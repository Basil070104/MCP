import os
from dotenv import load_dotenv
from pydantic import BaseModel
import httpx
import json
import logging
import asyncio

class WordWareTools():
  def __init__(self) -> None:
    load_dotenv()

    self.ww_key = os.environ.get("WORDWARE_API_KEY")
    self.app_id = os.environ.get("APP_ID")
    self.research_id = os.environ.get("RESEARCH_ID")
    self.base_url = "https://app.wordware.ai/api/released-app"
    
      
  async def save_notion(self, title:str, data:str):
    endpoint = f"{self.base_url}/005c038a-5a69-4cd6-a867-e2c48d8faa01/run"
    headers = {
      "Authorization": f"Bearer {self.ww_key}",
      "Content-Type": "application/json"
    }
    payload = {
      "inputs": {
          "title": title,
          "body": data,
      },
      "version": "^1.0"
    }
    
    response = httpx.post(endpoint, headers=headers, json=payload, timeout=90.0)
    
    if response.status_code == 200:
      # print("Success:", data_json.get("finalresearch", None))
      # return data_json.get("finalresearch", None)
      return "done"
    else:
      print(f"Error {response.status_code}: {response.text}")
      return None
    
  async def react_agent(self, question:str):
    endpoint = f"{self.base_url}/44ed8c26-1b67-4c07-9eb5-18b37b872fc7/run"
    headers = {
      "Authorization": f"Bearer {self.ww_key}",
      "Content-Type": "application/json"
    }
    payload = {
      "inputs": {
          "question": question,
      },
      "version": "^1.0"
    }
    
    response = httpx.post(endpoint, headers=headers, json=payload, timeout=90.0)
    
    data = response.text
    parsed_data = [json.loads(line) for line in data.strip().split('\n')]
    # print(parsed_data)
    output = parsed_data[-1]
    # print(output)
    value = output['value']
    id = value['values']
    final = id['answer']

    print(final)
    
    if response.status_code == 200:
      # print("Success:", data_json.get("finalresearch", None))
      # return data_json.get("finalresearch", None)
      return final
    else:
      print(f"Error {response.status_code}: {response.text}")
      return None

      
  async def research_founder(self, full_name: str, company: str, url: str):
    endpoint = f"{self.base_url}/{self.research_id}/run"
    headers = {
      "Authorization": f"Bearer {self.ww_key}",
      "Content-Type": "application/json"
    }
    payload = {
      "inputs": {
          "Full Name": full_name,
          "Company": company,
          "URL": url
      },
      "version": "^1.0"
    }
    
    logging.info("Processing Started > > >")

    response = httpx.post(endpoint, headers=headers, json=payload, timeout=90.0)
    
    # with open("test.json", "w") as f:

      
    data = response.text
    parsed_data = [json.loads(line) for line in data.strip().split('\n')]
    # print(parsed_data)
    # index = data.find("finalresearch")
    # cleaned_data = data[index:]
    # print(cleaned_data)
    with open("test.json", "w") as f:
      json.dump(parsed_data, f, indent=2)
      
    # if "finalresearch" in parsed_data:
    output = parsed_data[-3]
    value = output['value']
    id = value['output']
    final = id['finalresearchCompany']

    if response.status_code == 200:
      # print("Success:", data_json.get("finalresearch", None))
      # return data_json.get("finalresearch", None)
      return final
    else:
      print(f"Error {response.status_code}: {response.text}")
      return None
    
  async def enriching_leads(self, full_name: str, company: str, url: str):
    endpoint = f"{self.base_url}/51f53dfb-8575-4629-a430-7c48e3fbb2ec/run"
    headers = {
      "Authorization": f"Bearer {self.ww_key}",
      "Content-Type": "application/json"
    }
    payload = {
      "inputs": {
          "Full Name": full_name,
          "Company": company,
          "CompanyURL": url
      },
      "version": "^1.0"
    }
    
    response = httpx.post(endpoint, headers=headers, json=payload, timeout=90.0)
    
    data = response.text
    parsed_data = [json.loads(line) for line in data.strip().split('\n')]
    # print(parsed_data)
    output = parsed_data[-1]
    # print(output)
    value = output['value']
    # print(value)
    id = value['values']
    final = id['finalresearchCompany']
    
    if response.status_code == 200:
      print("Success:", final)
      return final
    else:
      print(f"Error {response.status_code}: {response.text}")
      return None
      
if __name__ == "__main__":
    tool = WordWareTools()
    # asyncio.run(tool.research_founder(full_name="Robert Chandler", company="Wordware", url="https://app.wordware.ai/lp"))
    # asyncio.run(tool.enriching_leads(full_name="Robert Chandler", company="Wordware", url="https://app.wordware.ai/lp"))
    # asyncio.run(tool.save_notion(title="Test", data="test"))
    asyncio.run(tool.react_agent(question="Give me information about kangaroos"))
