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

@app.post("/shops")
async def create_shop(shop: shops):
    # ouvrir le fichier json
    with open('data.json') as f:
        data = json.load(f)
        print(data)
    with open('data.json', mode="w") as f:
        data['shops'].append(shop.dict())
        f.write(json.dumps(data))
        print(data)
        # ajouter sneaker à la fin de la variable "data"
        # data.append(sneaker)
    # ecrire et fermer le fichier
    return "shop"














