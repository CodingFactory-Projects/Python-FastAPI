from fastapi import FastAPI
import json

with open('data.json') as f:
    data = json.load(f)

app = FastAPI()


@app.get("/data/sneakers")
async def get_sneakers():
    return data['sneakers']


@app.get("/data/sneakers/{sneaker_id}")
async def get_sneaker(sneaker_id: int):
    for sneaker in data['sneakers']:
        if sneaker_id == sneaker['id']:
            return sneaker
