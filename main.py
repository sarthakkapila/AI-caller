from fastapi import FastAPI
from tools.call_tool.py import CallNumber
app = FastAPI()

@app.post('/call')
async def root():
  return {'example' : 'This is an example', 'data':999}