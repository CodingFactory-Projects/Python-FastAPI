from fastapi import FastAPI
import json


app = FastAPI()

@app.get("/orders")
async def read_orders():
    with open('data.json','r') as f:
        orders = json.load(f)["orders"]
    return orders

