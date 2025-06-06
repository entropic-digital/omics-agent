import json
import logging
import uuid
import time
import threading
from typing import Optional, Dict, Any, List
from pydantic import BaseModel

import requests
import websocket
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse

from open_webui.utils.auth import get_verified_user


log = logging.getLogger(__name__)

router = APIRouter()

# Configuration
JUPYTER_VM_URL = "http://72.144.152.8:8888"


class CodeExecutionRequest(BaseModel):
    code: str
    timeout: Optional[int] = 30
    kernel_type: Optional[str] = "python3"


class CodeExecutionResponse(BaseModel):
    success: bool
    output: List[str]
    error: Optional[str] = None
    execution_time: Optional[float] = None
    kernel_id: Optional[str] = None


class JupyterKernelClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.kernel_id = None
        self.ws = None
        self.messages = []
        self.output_lines = []
        self.execution_complete = False
        self.error_occurred = False
        self.error_message = None
        
    def create_kernel(self) -> str:
        """Create a new kernel"""
        try:
            response = requests.post(f"{self.base_url}/api/kernels", timeout=10)
            response.raise_for_status()
            kernel_data = response.json()
            self.kernel_id = kernel_data['id']
            log.info(f"Created kernel: {self.kernel_id}")
            return self.kernel_id
        except Exception as e:
            log.error(f"Failed to create kernel: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to create kernel: {e}")
        
    def connect_websocket(self):
        """Connect to kernel WebSocket"""
        ws_url = f"ws://{self.base_url.split('//')[1]}/api/kernels/{self.kernel_id}/channels"
        
        def on_message(ws, message):
            try:
                data = json.loads(message)
                self.messages.append(data)
                
                # Handle execution results
                if data.get('msg_type') == 'stream':
                    content = data.get('content', {})
                    if 'text' in content:
                        self.output_lines.append(content['text'].strip())
                        
                elif data.get('msg_type') == 'execute_result':
                    content = data.get('content', {})
                    if 'data' in content:
                        text_data = content['data'].get('text/plain', '')
                        if text_data:
                            self.output_lines.append(f"Result: {text_data}")
                            
                elif data.get('msg_type') == 'error':
                    content = data.get('content', {})
                    self.error_occurred = True
                    self.error_message = f"{content.get('ename', 'Error')}: {content.get('evalue', 'Unknown error')}"
                    self.output_lines.append(f"ERROR: {self.error_message}")
                    
                elif data.get('msg_type') == 'status':
                    content = data.get('content', {})
                    if content.get('execution_state') == 'idle':
                        self.execution_complete = True
                        
            except Exception as e:
                log.error(f"Error processing WebSocket message: {e}")
        
        def on_error(ws, error):
            log.error(f"WebSocket error: {error}")
            self.error_occurred = True
            self.error_message = str(error)
            
        def on_close(ws, close_status_code, close_msg):
            log.info("WebSocket connection closed")
            
        try:
            self.ws = websocket.WebSocketApp(
                ws_url,
                on_message=on_message,
                on_error=on_error,
                on_close=on_close
            )
            
            # Start WebSocket in a separate thread
            ws_thread = threading.Thread(target=self.ws.run_forever)
            ws_thread.daemon = True
            ws_thread.start()
            
            # Wait for connection
            time.sleep(2)
            
        except Exception as e:
            log.error(f"Failed to connect WebSocket: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to connect to kernel: {e}")
        
    def execute_code(self, code: str, timeout: int = 30) -> Dict[str, Any]:
        """Execute code on the kernel"""
        if not self.ws:
            raise HTTPException(status_code=500, detail="WebSocket not connected")
            
        # Reset state
        self.output_lines = []
        self.execution_complete = False
        self.error_occurred = False
        self.error_message = None
        
        msg_id = str(uuid.uuid4())
        
        message = {
            "header": {
                "msg_id": msg_id,
                "msg_type": "execute_request",
                "username": "webui_user",
                "session": str(uuid.uuid4()),
                "date": time.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "version": "5.3"
            },
            "parent_header": {},
            "metadata": {},
            "content": {
                "code": code,
                "silent": False,
                "store_history": True,
                "user_expressions": {},
                "allow_stdin": False,
                "stop_on_error": True
            },
            "msg_id": msg_id,
            "msg_type": "execute_request"
        }
        
        start_time = time.time()
        
        try:
            self.ws.send(json.dumps(message))
            
            # Wait for execution to complete
            elapsed = 0
            while not self.execution_complete and elapsed < timeout:
                time.sleep(0.1)
                elapsed = time.time() - start_time
                
            execution_time = time.time() - start_time
            
            return {
                "success": not self.error_occurred,
                "output": self.output_lines,
                "error": self.error_message if self.error_occurred else None,
                "execution_time": execution_time,
                "kernel_id": self.kernel_id
            }
            
        except Exception as e:
            log.error(f"Error executing code: {e}")
            return {
                "success": False,
                "output": [],
                "error": str(e),
                "execution_time": time.time() - start_time,
                "kernel_id": self.kernel_id
            }
    
    def cleanup(self):
        """Clean up resources"""
        if self.ws:
            self.ws.close()


@router.post("/execute", response_model=CodeExecutionResponse)
async def execute_code(
    request: CodeExecutionRequest,
    user=Depends(get_verified_user)
):
    """
    Execute code on the remote Jupyter VM
    """
    log.info(f"Code execution request from user {user.email}: {len(request.code)} characters")
    
    client = None
    try:
        # Create Jupyter client
        client = JupyterKernelClient(JUPYTER_VM_URL)
        
        # Create kernel and connect
        client.create_kernel()
        client.connect_websocket()
        
        # Execute code
        result = client.execute_code(request.code, request.timeout or 30)
        
        log.info(f"Code execution completed: success={result['success']}, time={result['execution_time']:.2f}s")
        
        return CodeExecutionResponse(**result)
        
    except Exception as e:
        log.error(f"Code execution failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        if client:
            client.cleanup()


@router.get("/status")
async def get_vm_status(user=Depends(get_verified_user)):
    """
    Check if the remote VM is accessible
    """
    try:
        response = requests.get(f"{JUPYTER_VM_URL}/api/kernels", timeout=5)
        response.raise_for_status()
        kernels = response.json()
        
        return {
            "status": "online",
            "active_kernels": len(kernels),
            "vm_url": JUPYTER_VM_URL
        }
        
    except Exception as e:
        log.error(f"VM status check failed: {e}")
        return {
            "status": "offline",
            "error": str(e),
            "vm_url": JUPYTER_VM_URL
        }


@router.post("/execute/stream")
async def execute_code_stream(
    request: CodeExecutionRequest,
    user=Depends(get_verified_user)
):
    """
    Execute code with streaming response
    """
    async def generate():
        client = None
        try:
            client = JupyterKernelClient(JUPYTER_VM_URL)
            client.create_kernel()
            client.connect_websocket()
            
            yield f"data: {json.dumps({'type': 'status', 'message': 'Execution started'})}\n\n"
            
            result = client.execute_code(request.code, request.timeout or 30)
            
            # Stream output line by line
            for line in result['output']:
                yield f"data: {json.dumps({'type': 'output', 'content': line})}\n\n"
            
            if result['error']:
                yield f"data: {json.dumps({'type': 'error', 'content': result['error']})}\n\n"
            
            yield f"data: {json.dumps({'type': 'complete', 'success': result['success'], 'execution_time': result['execution_time']})}\n\n"
            
        except Exception as e:
            yield f"data: {json.dumps({'type': 'error', 'content': str(e)})}\n\n"
            
        finally:
            if client:
                client.cleanup()
    
    return StreamingResponse(generate(), media_type="text/plain")


# Bioinformatics-specific endpoints
@router.post("/execute/bioinformatics")
async def execute_bioinformatics_code(
    request: CodeExecutionRequest,
    user=Depends(get_verified_user)
):
    """
    Execute bioinformatics code with pre-configured environment setup
    """
    # Add common bioinformatics imports and setup
    setup_code = """
# Bioinformatics environment setup
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set up matplotlib for headless execution
plt.switch_backend('Agg')

# Common bioinformatics libraries (if available)
try:
    import scipy
    import sklearn
    print("✓ Scientific computing libraries loaded")
except ImportError as e:
    print(f"Some scientific libraries not available: {e}")

# Set working directory to user files (already mounted by start_runner.sh)
os.chdir('/user-files_host')
print(f"📂 Working directory: {os.getcwd()}")

# List available files
print("📁 Available files and directories:")
try:
    for item in os.listdir('.'):
        if os.path.isfile(item):
            size = os.path.getsize(item)
            print(f"  📄 {item} ({size:,} bytes)")
        elif os.path.isdir(item):
            print(f"  📁 {item}/")
    if not os.listdir('.'):
        print("  (no files found - upload files first)")
except Exception as e:
    print(f"  Error listing files: {e}")

# Helper functions for file operations
def list_files(pattern="*"):
    import glob
    return glob.glob(pattern)

def load_csv(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        print(f"File {filename} not found")
        return None

def load_tsv(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename, sep='\\t')
    else:
        print(f"File {filename} not found")
        return None

print("✅ Helper functions: list_files(), load_csv(), load_tsv()")
print("🧬 Bioinformatics environment ready!")
"""
    
    # Combine setup code with user code
    full_code = setup_code + "\n\n# User code:\n" + request.code
    
    # Create modified request
    bio_request = CodeExecutionRequest(
        code=full_code,
        timeout=request.timeout,
        kernel_type=request.kernel_type
    )
    
    return await execute_code(bio_request, user) 