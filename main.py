from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


"""Routes ROOT"""
@app.get("/")
async def root():
    return {"message": "Hello World"}


"""Routes USERS"""


"""Routes display name,age and short description"""
@app.get("/users/{name}/{age}")
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old " + str(age)+"years old."
    return {"name": name, "age": age, "description": name_with_age}

"""Routes display item with multiple query parameters"""
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

"""Routes display users with 3 query parameters"""
@app.get("/users/{item_id}")
async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item



"""Routes ITEMS"""

""" CREATE ITEMS with condition   """
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

"""Routes display item with query parameters (skip,limit)"""
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

"""Read item by item.id with condition for query paramaters"""
@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

"""Update all in item by item_id"""
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}

"""Routes PRODUITS"""

"""Routes display produit with required query parameters"""
@app.get("/produits/{item_id}")
async def read_user_item(item_id: str, requis: str):
    item = {"item_id": item_id, "requis": requis}
    return item


