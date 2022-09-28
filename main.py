from fastapi import FastAPI
from pydantic import BaseModel
import json
app = FastAPI()


class Order(BaseModel):
    products: dict
    client_id: int
    total_price: float | None = None
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/orders")
async def read_orders():
    with open('data.json','r') as f:
        orders = json.load(f)["orders"]
    return orders

@app.post("/orders/{order_id}")
async def create_orders(order_id: int, order: Order):
    result = {
        "order_id": order_id,
        "product": order.products,
        "client_id": order.client_id,
        "total_price": order.products["price"] * order.products["quantity"]
    }


    return result
