import os
import importlib
import logging
from typing import List, Dict, Any
from pathlib import Path

log = logging.getLogger(__name__)


def load_all_tools() -> List[Dict[str, Any]]:
    """
    Automatically load all tools from the bioinformatics-mcp directory.
    Returns a list of tool dictionaries containing name, function, and
    metadata.
    """
    tools_dir = (
        Path(__file__).parent.parent.parent.parent / 
        'bioinformatics_mcp'
    )
    loaded_tools = []
    
    try:
        # First, import the tool_decorator to initialize the registration system
        importlib.import_module('bioinformatics_mcp.tool_decorator')
        
        # Walk through all directories in the bioinformatics-mcp folder
        for item in os.listdir(tools_dir):
            if item in {
                '__pycache__', '.git', '.pytest_cache',
                '__init__.py', 'tool_decorator.py', 'core'
            } or item.startswith('.'):
                continue
                
            if (tools_dir / item).is_dir():
                # Try to import the tool module
                try:
                    # Import the tool module
                    module_path = f"bioinformatics_mcp.{item}"
                    importlib.import_module(module_path)
                    
                    # Look for MCP run modules in this tool directory
                    mcp_dir = tools_dir / item / 'mcp'
                    if mcp_dir.exists():
                        for run_file in mcp_dir.glob('run_*.py'):
                            try:
                                # Import the run module
                                module_name = (
                                    f"bioinformatics_mcp.{item}.mcp."
                                    f"{run_file.stem}"
                                )
                                importlib.import_module(module_name)
                            except Exception as e:
                                log.error(
                                    f"Failed to load run module "
                                    f"{run_file}: {str(e)}"
                                )
                except Exception as e:
                    log.error(f"Failed to load tool module {item}: {str(e)}")
        
        # After loading all modules, collect the registered tools
        from bioinformatics_mcp.tool_decorator import tool_functions
        loaded_tools = tool_functions
        
        # Initialize the tools in the manager
        from .tools_manager import tools_manager
        tools_manager._initialize_tools(loaded_tools)
        
        return loaded_tools
        
    except Exception as e:
        log.error(f"Error loading tools: {str(e)}")
        return [] 