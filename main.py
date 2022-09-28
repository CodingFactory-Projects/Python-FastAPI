from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

import json

app = FastAPI()

class shops(BaseModel):
    shop_id: int
    country: str
    city: str
    adresse: str
    proprietaire: str
    loyer: Optional[float] = None

#inventory = {}

#@app.get("/get_shops/")
#async def get_all_shops():
    #return inventory

#@app.get("/get_shop/{shop_id}")
#async def get_shop(shop_id: int = Path(None, description="The ID of the shop you would like to view")):
    #return inventory[shop_id]

@app.get("/shops")
async def get_shops():
    with open('data.json') as f:
        data = json.load(f)
        return data['shops']

@app.get("/shops/{shop_id}")
async def get_shop(shop_id: int):
    with open('data.json') as f:
        data = json.load(f)
    for shop in data['shops']:
        if shop_id == shop['shop_id']:
            return shop














