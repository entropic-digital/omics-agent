import logging
import os
import importlib
from pathlib import Path


def find_mcp_run_modules(tool_dir_path):
    """Recursively find all mcp directories containing run_*.py files."""
    found_modules = []

    # Convert to Path object for easier manipulation
    tool_path = Path(tool_dir_path)

    # Find all mcp directories
    for mcp_dir in tool_path.rglob("mcp"):
        # Look for run_*.py files in the mcp directory
        for run_file in mcp_dir.glob("run_*.py"):
            # Convert the file path to a module path
            rel_path = run_file.relative_to(
                Path(os.path.dirname(os.path.dirname(__file__)))
            )
            module_path = f"{str(rel_path).replace(os.sep, '.')[:-3]}"
            found_modules.append(module_path)

    return found_modules


def load_all_tools():
    """Load all tool modules to collect decorated functions."""
    tools_dir = os.path.dirname(__file__)

    # Go through all tools
    for tool_dir in os.listdir(tools_dir):
        if tool_dir.startswith("__"):
            continue

        tool_dir_path = os.path.join(tools_dir, tool_dir)
        if not os.path.isdir(tool_dir_path):
            continue

        # Find all possible module paths for this tool
        module_paths = find_mcp_run_modules(tool_dir_path)

        # Try to import each found module
        for module_path in module_paths:
            try:
                importlib.import_module(module_path)
            except ImportError as e:
                logging.error(f"Error importing {module_path}: {e}")


# Load all tools when this package is imported
load_all_tools()

# Export the collected tools
from .tool_decorator import tool_functions
