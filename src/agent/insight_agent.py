from google.adk.agents import Agent, SequentialAgent, App
from src.tools.mospi_client import mospi_tools
from .prompts import DATA_RESEARCHER_SYSTEM_PROMPT, TREND_ANALYST_SYSTEM_PROMPT

# Define the model - ensure you are using a valid string
MODEL_NAME = "gemini-2.0-flash"

data_researcher = Agent(
    name="DataResearcher",
    model=MODEL_NAME,
    instructions=DATA_RESEARCHER_SYSTEM_PROMPT,
    tools=[mospi_tools]
)

trend_analyst = Agent(
    name="TrendAnalyst",
    model=MODEL_NAME,
    instructions=TREND_ANALYST_SYSTEM_PROMPT
)

# Create the Sequential Flow
india_insight_agent = SequentialAgent(
    name="india_insight_agent",
    agents=[data_researcher, trend_analyst]
)

# This 'app' or 'root_agent' export is what get_fast_api_app looks for
app = App(
    name="india_insight_app",
    root_agent=india_insight_agent
)

root_agent = india_insight_agent