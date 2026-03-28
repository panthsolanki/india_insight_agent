from fastmcp import Client

# ✅ Correct MCP endpoint
MCP_URL = "https://mcp.mospi.gov.in/mcp"

client = Client(MCP_URL)


def get_cpi():
    return client.call("get_data", {
        "dataset": "CPI"
    })


def get_gdp():
    return client.call("get_data", {
        "dataset": "GDP"
    })


def get_employment():
    return client.call("get_data", {
        "dataset": "PLFS"
    })