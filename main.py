from datetime import datetime

from fastapi import FastAPI

import json

from typing import List, Optional

from pydantic import BaseModel

app = FastAPI()

with open('data.json') as f:
    data = json.load(f)


@app.get("/")
async def root():
    return {"message": "Hello World"}, data


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
