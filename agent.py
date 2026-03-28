from google.adk.agents import LlmAgent
from google.adk.tools import tool
from mcp_wrapper import mcp_wrapper

@tool
def fetch_india_data(query: str):
    """
    Explore datasets and fetch relevant India development data
    """
    return mcp_wrapper.query(query)


agent = LlmAgent(
    name="india_dev_agent",
    instruction="""
    You explain India's development in very simple English.

    Process:
    1. ALWAYS call fetch_india_data
    2. Use selected_dataset to understand context:
    - CPI → inflation
    - GDP → economic growth
    - PLFS → employment

    3. Explain:
    - What is happening
    - Why it matters to people

    Rules:
    - Keep under 5 sentences
    - No jargon
    - Be clear and simple
    """,
    tools=[fetch_india_data],
)