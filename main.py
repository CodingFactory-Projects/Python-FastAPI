from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

import json

app = FastAPI()

#creating a class shops thats gonna be usefull to create our shops

class shops(BaseModel):
    shop_id: int
    country: str
    city: str
    adresse: str
    proprietaire: str
    loyer: Optional[float] = None


#Here we have the "get" methods

@app.get("/shops")
async def get_shops():
    with open('data.json') as f:
        data = json.load(f)
        return data['shops']

@app.get("/shop/{shop_id}")
async def get_shop(shop_id: int):
    with open('data.json') as f:
        data = json.load(f)
    for shop in data['shops']:
        if shop_id == shop['shop_id']:
            return shop

#Here we have the "post" methods

@app.post("/shops")
async def create_shop(shop: shops):
    # ouvre le json
    with open('data.json') as f:
        data = json.load(f)
        print(data)
    with open('data.json', mode="w") as f:
        data['shops'].append(shop.dict())
        f.write(json.dumps(data))
        print(data)
    return "shop"


@app.delete("/shops")
async def delete_shop(shop_id: int):
    with open('data.json') as f:
        data = json.load(f)
    for shop in data['shops']:
        if shop_id == shop['shop_id']:
            data['shops'].remove(shop)
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data))
            return data['shops']
        else:
            return {"message": "existe pas"}














