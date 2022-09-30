from fastapi import FastAPI, HTTPException
import json
from classes.SneakersClass import Sneakers, EditedSneaker

app = FastAPI()

data = json.load(open('data.json'))


def write_data():
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2, separators=(',', ': '))


@app.get("/data")
async def get_data():
    return data


@app.get("/sneakers")
async def get_sneakers():
    return data['sneakers']


@app.get("/sneakers/{sneaker_id}")
async def get_sneaker(sneaker_id: int):
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id matches the id in the url return the sneaker info
        if sneaker_id == sneaker['id']:
            return sneaker
    return HTTPException(status_code=404, detail="Sneaker not found")


@app.get("/sneakers/name/{sneaker_id}")
async def get_sneaker_name(sneaker_id: int):
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id matches the id in the url return the sneakers name
        if sneaker_id == sneaker['id']:
            return sneaker["name"]
    return HTTPException(status_code=404, detail="Sneaker not found")


# POST METHOD
@app.post("/sneakers")
async def create_sneaker(new_sneaker: Sneakers):
    new_sneaker.id = data['sneakers'][-1]['id'] + 1
    # add the new sneaker to the data
    if new_sneaker.id not in [sneaker['id'] for sneaker in data['sneakers']]:
        data['sneakers'].append(new_sneaker.dict())
        write_data()
        return "Sneaker has been added"
    return HTTPException(status_code=404, detail="Sneaker already exists")


@app.put("/sneakers/{sneaker_id}")
async def update_sneaker(sneaker_id: int, edited_sneaker: EditedSneaker):
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id is the same as the sneaker id in the url
        if sneaker['id'] == sneaker_id:
            sneaker['name'] = edited_sneaker.name or sneaker['name']
            sneaker['img'] = edited_sneaker.img or sneaker['img']
            sneaker['description'] = edited_sneaker.description or sneaker['description']
            sneaker['colors'] = edited_sneaker.colors or sneaker['colors']
            sneaker['price'] = edited_sneaker.price or sneaker['price']
            sneaker['stock'] = edited_sneaker.stock or sneaker['stock']
            write_data()
            return "Sneaker as been updated"
    return HTTPException(status_code=404, detail="Sneaker not found")


@app.delete('/sneaker/{sneaker_id}')
async def delete_sneaker(sneaker_id: int):
    # loop through the sneakers and find the sneaker with the id given
    for sneaker in data['sneakers']:
        if sneaker_id == sneaker['id']:
            data['sneakers'].remove(sneaker)
            write_data()
            return "Sneaker has been deleted"
    return HTTPException(status_code=404, detail="Sneaker not found")
