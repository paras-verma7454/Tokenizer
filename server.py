
from fastapi import FastAPI
import tiktoken 


enc = tiktoken.encoding_for_model("gpt-4o")

app= FastAPI()

@app.get("/")
def hello():
    return "Write a string after / like this    /hello world"


@app.get("/{str}")
def read(str):
    return{"Tokens":f"{enc.encode(str)}",
            "Decoded":f"{str}"}

# fastapi dev server.py to start the server