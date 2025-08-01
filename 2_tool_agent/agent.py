import datetime
from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
    """
    Get the current time in the format YYYY-MM-DD HH:MM:SS
    """
    return {
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    

root_agent = Agent(
  name="tool_agent",
  model="gemini-2.0-flash",
  description="Tools agent",
  instruction=("""
      You are a helpful assistant that can use the following tools:
    - get_current_time for get current date time
    - google_search
  """),
  tools=[get_current_time]
  # tools=[google_search]
)
