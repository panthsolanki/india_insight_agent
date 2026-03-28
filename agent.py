from google.adk.agents import LlmAgent
from google.adk.tools import tool

from mcp_client import get_cpi, get_gdp, get_employment


@tool
def fetch_inflation():
    """Fetch inflation (CPI) data"""
    return get_cpi()


@tool
def fetch_gdp():
    """Fetch GDP data"""
    return get_gdp()


@tool
def fetch_employment():
    """Fetch employment data"""
    return get_employment()


agent = LlmAgent(
    name="india_dev_agent",
    instruction="""
You explain India's development in very simple English.

Rules:
- ALWAYS use tools to get real data
- Choose correct tool:
  - fetch_inflation → inflation
  - fetch_gdp → growth
  - fetch_employment → jobs

- Then:
  1. Identify trend
  2. Explain in simple terms
  3. Keep under 5 sentences
""",
    tools=[fetch_inflation, fetch_gdp, fetch_employment],
)