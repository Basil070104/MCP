import os
from dotenv import load_dotenv

import asyncio
from swerex.deployment.local import LocalDeployment
from swerex.runtime.abstract import CreateBashSessionRequest, BashAction, Command
import asyncio
import json

from typing import Any, List, Set
import httpx
from mcp.server.fastmcp import FastMCP



load_dotenv() 

ww_key = os.environ.get('WORDWARE_API_KEY')
app_id = os.environ.get('APP_ID')

deployment = LocalDeployment()

asyncio.run(deployment.start())

runtime = deployment.runtime

asyncio.run(runtime.create_session(CreateBashSessionRequest()))

command = f"""curl 'https://api.wordware.ai/v1/apps/{app_id}' \
  --header 'Authorization: Bearer {ww_key}'"""
  
output = asyncio.run(runtime.run_in_session(BashAction(command=command)))
result = output.output

# print(json.loads(result))

with open("app.json", "w") as f:
  json.dump(json.loads(result), f)

asyncio.run(deployment.stop())

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"
