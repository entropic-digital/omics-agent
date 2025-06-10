import logging
from typing import List, Dict, Callable, Any


class ToolsManager:
    def __init__(self):
        self._tools: Dict[str, Callable] = {}
        # Don't initialize tools in constructor
        self._tools = {}

    def _initialize_tools(self, tool_functions):
        """Initialize all tools from the provided tool functions"""
        for tool in tool_functions:
            self.add_tool(tool["function"], name=tool["name"])

    def add_tool(self, tool_function: Callable, name: str = None):
        """Add a tool to the manager"""
        if name is None:
            name = tool_function.__name__
        self._tools[name] = tool_function

    def get_tool(self, name: str) -> Callable:
        """Get a tool by name"""
        return self._tools.get(name)

    def list_tools(self) -> List[str]:
        """List all available tools"""
        return list(self._tools.keys())

    async def execute_tool(self, tool_name: str, **kwargs) -> Any:
        """Execute a tool by name with given arguments"""
        tool = self.get_tool(tool_name)
        if tool is None:
            raise ValueError(f"Tool {tool_name} not found")

        try:
            result = tool(**kwargs)
            return result
        except Exception as e:
            logging.error(f"Error executing tool {tool_name}: {str(e)}")
            raise


# Create a global instance of the tools manager
tools_manager = ToolsManager()


def load_all_tools():
    """
    Load all tools using the new bio_mcp.tools.tool_manager interface.
    """
    from bio_mcp.tools.tool_manager import get_registered_tools

    loaded_tools = get_registered_tools()
    from .tools_manager import tools_manager

    tools_manager._initialize_tools(loaded_tools)
    return loaded_tools
