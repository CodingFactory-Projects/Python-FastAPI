from fastapi import FastAPI, HTTPException
from classes.ShopsClass import shops

import json

app = FastAPI()


# creating a class shops thats gonna be usefull to create our shops


# Here we have the "get" methods
# Get all shops
@app.get("/shops")
async def get_shops():
    # opening and loading the json
    with open('data.json') as f:
        data = json.load(f)
        return data['shops']


# Get a specific shop by id
@app.get("/shop/{shop_id}")
async def get_shop(shop_id: int):
    with open('data.json') as f:
        data = json.load(f)
    for shop in data['shops']:
        if shop_id == shop['shop_id']:
            return shop


# Here we have the "post" methods
# We can create new shops
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


# Here we have the "post" methods
# We can delete existing shops
# If the shop already exists, we can delete it, otherwise if it doesnt, we cannot delete it so an error is returned
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
    return HTTPException(status_code=404, detail="Shop doesnt exist")
