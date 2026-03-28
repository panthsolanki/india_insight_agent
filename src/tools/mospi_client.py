import os
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams
# from google.adk.tools.mcp_tool import MCPToolset

# The official MoSPI MCP endpoint
MOSPI_URL = "https://mcp.mospi.gov.in/sse"

def get_mospi_tools():
    """
    Initializes the MCP Toolset to connect to the 
    public eSankhyiki MCP server.
    """
    # We use StreamableHTTPConnectionParams for web-hosted (SSE) MCP servers
    connection_params = StreamableHTTPConnectionParams(
        url=MOSPI_URL
    )
    
    # Create the toolset that our agents will use
    toolset = MCPToolset(
        name="mospi_official_tools",
        connection_params=connection_params
    )
    
    return toolset

# Export a single instance for the agents to import
mospi_tools = get_mospi_tools()