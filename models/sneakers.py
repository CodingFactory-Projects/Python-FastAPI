from fastapi import FastAPI
import json

with open('data.json') as f:
    data = json.load(f)

app = FastAPI()


@app.get("/data/sneakers")
async def get_sneakers():
    return data['sneakers']

