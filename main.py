from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
async def read_root():
    return {"message": "Добро пожаловать в простой FastAPI сервер!"}