import os
import importlib
import logging
from typing import List, Dict, Any
from pathlib import Path

log = logging.getLogger(__name__)


def load_all_tools() -> List[Dict[str, Any]]:
    """
    Automatically load all tools from the tools directory.
    Returns a list of tool dictionaries containing name, function, and
    metadata.
    """
    tools_dir = (
        Path(__file__).parent.parent.parent.parent / 'tools'
    )
    loaded_tools = []
    
    try:
        # First, import the tool_decorator to initialize the registration system
        importlib.import_module('tools.tool_decorator')
        
        # Walk through all directories in the tools folder
        for item in os.listdir(tools_dir):
            if item in {
                '__pycache__', '.git', '.pytest_cache',
                '__init__.py', 'tool_decorator.py'
            } or item.startswith('.'):
                continue
                
            if (tools_dir / item).is_dir():
                # Try to import the tool module
                try:
                    # Import the tool module
                    module_path = f"tools.{item}"
                    importlib.import_module(module_path)
                    
                    # Look for MCP run modules in this tool directory
                    mcp_dir = tools_dir / item / 'mcp'
                    if mcp_dir.exists():
                        for run_file in mcp_dir.glob('run_*.py'):
                            try:
                                # Import the run module
                                module_name = (
                                    f"tools.{item}.mcp.{run_file.stem}"
                                )
                                importlib.import_module(module_name)
                            except Exception as e:
                                log.error(
                                    f"Failed to load run module {run_file}: {str(e)}"
                                )
                except Exception as e:
                    log.error(f"Failed to load tool module {item}: {str(e)}")
        
        # After loading all modules, collect the registered tools
        from tools.tool_decorator import tool_functions
        loaded_tools = tool_functions
        
        # Initialize the tools in the manager
        from .tools_manager import tools_manager
        tools_manager._initialize_tools(loaded_tools)
        
        return loaded_tools
        
    except Exception as e:
        log.error(f"Error loading tools: {str(e)}")
        return [] 