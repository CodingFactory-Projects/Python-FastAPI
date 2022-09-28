import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/orders")
async def get_orders():
    with open('data.json','r') as f:
        orders = json.load(f)["orders"]
    return orders
