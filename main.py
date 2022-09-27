from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Shop(BaseModel):
    country: str
    city: str
    adresse: str
    proprietaire: str
    loyer: Optional[float] = None


inventory = {}

@app.get("/get_shop/{shop_id}")
async def get_shop(shop_id: int = Path(None, description="The ID of the shop you would like to view")):
    return inventory[shop_id]

@app.post("/create_shop/{shop_id}")
async def create_shop(shop_id: int, shop: Shop):
    if shop_id in inventory:
        return {"Error": "Shop already exists."}

    inventory[shop_id] = shop
    return inventory[shop_id]

