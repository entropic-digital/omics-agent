from typing import Callable, List, Dict
from functools import wraps

# Store for all decorated functions
tool_functions: List[Dict[str, Callable]] = []


def collect_tool():
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        # Get the module path and extract the tool name
        module_parts = func.__module__.split('.')
        
        # Find the parent tool name from the module path
        # Example paths: tools.samtools.index, tools.bamtools.filter
        if len(module_parts) >= 2:
            parent_tool = module_parts[1]  # tools.{parent_tool}.function
            unique_name = f"{parent_tool}_{func.__name__}"
        else:
            # Standalone tools without a parent
            unique_name = func.__name__
        
        # Store the function and its metadata
        tool_functions.append(
            {"name": unique_name, "function": func, "doc": func.__doc__}
        )
        return wrapper

    return decorator
