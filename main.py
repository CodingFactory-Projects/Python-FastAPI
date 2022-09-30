from fastapi import FastAPI
from pydantic import BaseModel
import json
app = FastAPI()

#class girl
class Products(BaseModel):
    product_id: int
    price: float
    quantity: int
# Parent class
class Order(BaseModel):
    id_order: int
    products: list[Products] | Products
    total_price: int | None
    client_id: int

#Allows us to retrieve our commands in our json file
def recupJson():
    with open('data.json','r') as f:
        orders = json.load(f)
    return orders
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

#Get all commands from json
@app.get("/orders")
async def read_orders():
    data =recupJson()
    return data["orders"]

#Retrieves orders based on its id
@app.get("/orders/{id_order}")
async def get_orders_by_order_id(id_order: int):
    data = recupJson()
    for x in data["orders"]:
        if x["id_order"] == id_order:
           return x
    return "Not found"

#Update command thanks to its id_order
@app.patch("/orders")
async def update_orders_by_order_id(order: Order):
    data = recupJson()
    for x in data["orders"]:
        if x["id_order"] == order.id_order:
            order.total_price = order.products.price * order.products.quantity
            with open('data.json', 'w') as f:
                data["orders"].remove(x)
                data["orders"].append(order.dict())
                f.write(json.dumps(data, sort_keys=True, indent=4))
    return "Not found"

#Allows you to create an order
@app.post("/orders")
async def create_order(order: Order):
    data = recupJson()
    for x in data["orders"]:
        if x["id_order"] == order.id_order:
            return "Your id_order is already use. Try again"
        else:
            order.total_price = order.products.price * order.products.quantity
            with open('data.json','w') as f:
                data["orders"].append(order.dict())
                f.write(json.dumps(data, sort_keys=True, indent=4))
        return "Your order has been registered "
#Allows you to delete an order
@app.delete("/orders/{id_order}")
async def delete_order(id_order: int):
    data = recupJson()
    for x in data["orders"]:
        if x["id_order"] == id_order:
            with open('data.json', 'w') as f:
                data["orders"].remove(x)
                f.write(json.dumps(data, sort_keys=True, indent=4))
    return "Your order has been deleted "
#Allows you to delete all order
@app.delete("/orders")
async def delete_all_orders():
    data = recupJson()
    for x in data["orders"]:
        with open('data.json', 'w') as f:
            data["orders"].clear()
            f.write(json.dumps(data, sort_keys=True, indent=4))
    return "Your orders has been deleted "
