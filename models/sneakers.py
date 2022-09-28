from fastapi import FastAPI
import json

from pydantic import BaseModel

app = FastAPI()


class Sneakers(BaseModel):
    id: int
    img: str
    name: str
    description: str
    colors: str
    price: str
    stock: str


@app.get("/data")
async def get_data():
    with open('data.json') as f:
        data = json.load(f)
        return data


@app.get("/sneakers")
async def get_sneakers():
    with open('data.json') as f:
        data = json.load(f)
    return data['sneakers']


@app.get("/sneakers/{sneaker_id}")
async def get_sneaker(sneaker_id: int):
    with open('data.json') as f:
        data = json.load(f)
    for sneaker in data['sneakers']:
        if sneaker_id == sneaker['id']:
            return sneaker


@app.get("/sneakers/name/{sneaker_id}")
async def get_sneaker_name(sneaker_id: int):
    with open('data.json') as f:
        data = json.load(f)
    for sneaker in data['sneakers']:
        if sneaker_id == sneaker['id']:
            return sneaker["name"]

# POST METHODS

@app.post("/sneakers")
async def create_sneaker(sneaker: Sneakers):
    # ouvrir le fichier json
    with open('data.json') as f:
        data = json.load(f)
    with open('data.json', mode="w") as f:
        data['sneakers'].append(sneaker.dict())
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))
        print(data)
    return data
