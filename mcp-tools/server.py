from fastapi import FastAPI
from tools import WordWareTools

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/research_founders")
async def get_tools():
  tools = WordWareTools()
  return {"message": "Tools"}
