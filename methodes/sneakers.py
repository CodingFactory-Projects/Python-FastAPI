from fastapi import FastAPI, HTTPException
import json
from classes.SneakersClass import Sneakers, EditedSneaker

app = FastAPI()


@app.get("/data")
async def get_data():
    # get all data from json file
    with open('data.json') as f:
        data = json.load(f)
        return data


@app.get("/sneakers")
async def get_sneakers():
    # get all sneakers from json file
    with open('data.json') as f:
        data = json.load(f)
    return data['sneakers']


@app.get("/sneakers/{sneaker_id}")
async def get_sneaker(sneaker_id: int):
    # open the json file and load the data
    with open('data.json') as f:
        data = json.load(f)
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id matches the id in the url return the sneaker info
        if sneaker_id == sneaker['id']:
            return sneaker
    return HTTPException(status_code=404, detail="Sneaker not found")


@app.get("/sneakers/name/{sneaker_id}")
async def get_sneaker_name(sneaker_id: int):
    # open the json file and load the data
    with open('data.json') as f:
        data = json.load(f)
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id matches the id in the url return the sneakers name
        if sneaker_id == sneaker['id']:
            return sneaker["name"]
    return HTTPException(status_code=404, detail="Sneaker not found")


# POST METHODS

@app.post("/sneakers")
async def create_sneaker(sneaker: Sneakers):
    # open the json file and load the data
    with open('data.json') as f:
        data = json.load(f)
    # with the jso file open in write mode add the new sneaker to the data
    with open('data.json', mode="w") as f:
        data['sneakers'].append(sneaker.dict())
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))
        return "Sneaker has been added"


@app.put("/sneakers/{sneaker_id}")
async def update_sneaker(sneaker_id: int, edited_sneaker: EditedSneaker):
    # open the json file and load the data
    with open('data.json') as f:
        data = json.load(f)
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
            with open('data.json', mode="w") as f:
                # write the new data to the json file
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                return "Sneaker as been updated"
    return HTTPException(status_code=404, detail="Sneaker not found")


@app.delete('/sneaker/{sneaker_id}')
async def delete_sneaker(sneaker_id: int):
    # open the json file and load the data
    with open('data.json') as f:
        data = json.load(f)
    # loop through the sneakers and find the sneaker with the id given
    for sneaker in data['sneakers']:
        if sneaker_id == sneaker['id']:
            data['sneakers'].remove(sneaker)
            with open('data.json', mode="w") as f:
                # write the new data to the json file
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                print(data)
            return "Sneaker has been deleted"
    return HTTPException(status_code=404, detail="Sneaker not found")
