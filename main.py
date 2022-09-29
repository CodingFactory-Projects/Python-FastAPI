from fastapi import FastAPI
from pydantic import BaseModel
import json
app = FastAPI()


class Order(BaseModel):
    products: dict
    client_id: int
    total_price: float | None = None

#Permet de récupérer nos commandes dans notre ficheir json
def recupJson():
    with open('data.json','r') as f:
        orders = json.load(f)["orders"]
    return orders
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
#Recupere toutes les commandes du json
@app.get("/orders")
async def read_orders():
    return recupJson()

#Recupere les commandes en fonction de son id
@app.get("/orders/{order_id}")
async def get_orders_by_order_id(order_id: int):
    data = recupJson()
    print(type(data))
    for x in data:
        if x["order_id"] == order_id :
           return x
    return "Nothing here"


#Permet de créer une commande
@app.post("/orders")
async def create_user(user: Order):
    data = recupJson()
    with open('data.json', mode='w') as f:
        data['orders'].append(user.dict())
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))
    return 'user'
