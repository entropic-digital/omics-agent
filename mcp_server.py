import sys
import logging
from mcp.server.fastmcp import FastMCP
from tools import tool_functions

logging.basicConfig(level=logging.INFO)

# Initialize MCP server
mcp = FastMCP("Omics-Agent-MCP")

# Register all collected tools
for tool in tool_functions:
    mcp._tool_manager.add_tool(tool["function"], name=tool["name"])

if __name__ == "__main__":
    try:
        logging.info("Starting MCP server with stdio transport...")
        available_tools = mcp._tool_manager.list_tools()
        logging.info(f"There are {len(available_tools)} available tools")
        mcp.run(transport="stdio")
    except Exception as e:
        logging.error(f"Error starting MCP server: {str(e)}")
        sys.exit(1)