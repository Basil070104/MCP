import os
from dotenv import load_dotenv
from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP

class WordWareTools(BaseModel):
  def __init__(self) -> None:
    load_dotenv()

    self.ww_key = os.environ.get("WORDWARE_API_KEY")
    self.app_id = os.environ.get("APP_ID")
    self.research_id = os.environ.get("RESEARCH_ID")

    self.mcp = FastMCP("Wordware")
    
    self.mcp.tool()(self.research_found)

  def research_found(self):
      # Add actual functionality here
      print("Research found tool called.")
