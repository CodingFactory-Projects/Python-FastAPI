from fastapi import FastAPI
from typing import Union
import pydantic
print('compiled:', pydantic.compiled)

#from pydantic import BaseMode1

app = FastAPI()

#class Item(BaseMode1):
    #name: str
    #price: float
    #is_offer: Union[bool, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item-id": item_id, "q": q}

@app.get("/users")
async def red_users():
    return ["Rick"]

from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    louis = "louis"
    alan = "alan"
    moha = "moha"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.louis:
        return {"model_name": model_name, "message": "chinois de la caille"}

    if model_name.value == "alan":
        return {"model_name": model_name, "message": "onizuka"}

    return {"model_name": model_name, "message": "clito"}


#@app.put("/items/{item_id}")
#async def update_item(item_id: int, item: Item):
    #return {"item_id": item_id, "item_name": item.name}

