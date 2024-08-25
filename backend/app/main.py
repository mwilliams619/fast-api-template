from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Hello World API")

class Message(BaseModel):
    message: str

@app.get("/", response_model=Message)
def read_root():
    return {"message": "Hello, World!"}

@app.get("/env", response_model=Message)
def read_environment():
    # Just to demonstrate environment variable usage
    environment = os.getenv("FASTAPI_ENV", "development")
    return {"message": f"Running in {environment} environment"}

#debug