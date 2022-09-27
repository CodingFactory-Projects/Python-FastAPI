from fastapi import FastAPI
from typing import Union
from pydantic import BaseMode1

app = FastAPI()

class Item(BaseMode1):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item-id": item_id, "q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}

