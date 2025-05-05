from fastapi import FastAPI
from tools import WordWareTools
from pydantic import BaseModel

app = FastAPI()

class FounderRequest(BaseModel):
    full_name: str
    company: str
    website: str
    
class Question(BaseModel):
    question: str



@app.get("/")
async def root():
    return {"message": "Hello World"}
  
@app.post("/react_agent")
async def react_agent(request: Question):
  tools = WordWareTools()
  print(request)
  results = await tools.react_agent(
        question=request.question,
    )
  print("here2")

  return {"message": results}

@app.post("/research_founders")
async def research_founders(request: FounderRequest):
  tools = WordWareTools()
  print(request)
  results = await tools.research_founder(
        full_name=request.full_name,
        company=request.company,
        url=request.website
    )
  print("here2")

  return {"message": results}

@app.post("/personalized_questions")
async def personalized_questions(request: FounderRequest):
  tools = WordWareTools()
  response = tools.research_founder(
        full_name=request.full_name,
        company=request.company,
        url=request.website
    )

  return {"message": "Received from MPC Server"}


@app.post("/person_research")
async def person_research(request: FounderRequest):
  tools = WordWareTools()
  response = tools.research_founder(
        full_name=request.full_name,
        company=request.company,
        url=request.website
    )

  return {"message": "Received from MPC Server"}

@app.post("/competition_research")
async def competition_research(request: FounderRequest):
  tools = WordWareTools()
  response = tools.research_founder(
        full_name=request.full_name,
        company=request.company,
        url=request.website
    )

  return {"message": "Received from MPC Server"}

@app.post("/company_research")
async def company_research(request: FounderRequest):
  tools = WordWareTools()
  response = tools.research_founder(
        full_name=request.full_name,
        company=request.company,
        url=request.website
    )

  return {"message": "Received from MPC Server"}

@app.post("/enriching_leaders")
async def enriching_leaders(request: FounderRequest):
  tools = WordWareTools()
  response = await tools.enriching_leads(
        full_name=request.full_name,
        company=request.company,
        url=request.website
    )

  return {"message": response}

