from fastapi import FastAPI
from typing import Union
from enum import Enum
from pydantic import BaseModel

# from pydantic import BaseMode1

app = FastAPI()


# class Item(BaseMode1):
# name: str
# price: float
# is_offer: Union[bool, None] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item-id": item_id, "q": q}


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
# return {"item_id": item_id, "item_name": item.name}

@app.get("/users")
async def red_users():
    return ["Rick"]


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


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/names/{item_id}")
async def read_name(item_id: str, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


class Numbers(BaseModel):
    id: int
    name: str
    price: float

data = {
    'countries': [

    ]
}
#@app.post("/countries/{country_name}")
#async def create_country(country_name: str):
    #if country_name in data["countries"]:
        #return {"data": data, "message": "déjà existant"}

    #else:
        #data["countries"].append(country_name)
        #return {"data": data, "message": "a été ajouté"}

#@app.delete("/countries/{country_name}")
#async def delete_country(country_name: str):
    #if country_name in data["countries"]:
        #data["countries"].remove(country_name)
        #return {"data": data, "message": "a été supprimé"}

    #else:
        #return {"data": data, "message": "non existant"}