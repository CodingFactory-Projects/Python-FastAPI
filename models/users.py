from fastapi import FastAPI
import json

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


def load_data():
    with open('data.json') as f:
        return json.load(f)


data = load_data()


# Function to get users from data.json

@app.get("/users/")
async def get_users():
    return data['users']


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    for user in data['users']:
        if user_id == user['id']:
            return user


# Function to post users from data.json

class User(BaseModel):
    id: int | None = None
    username: str
    money: int | None = None


@app.post("/users/")
async def create_user(user: User):
    with open('data.json', mode='w') as f:
        data['users'].append(user.dict())
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))
    return 'user'


# Function to delete users by id

@app.delete("/users/{user_id}")
async def delete_users(user_id: int):
    for user in data['users']:
        if user_id == user['id']:
            data['users'].remove(user)
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                print(data)
            return data


# Function to modify 1 element of users info by id

@app.patch("/users/{user_id}")
async def update_user(user_id: int, user: User):
    for users in data['users']:
        if user_id == users['id']:
            stored_user_data = users
            stored_user_model = User(**stored_user_data)
            update_data = user.dict(exclude_unset=True)
            stored_user_model.copy(update=update_data)
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                return update_data


@app.put("/users/{user_id}")
async def update_user_all(user_id: int, user: User):
    for users in data['users']:
        if users['id'] == user_id:
            users['username'] = user.username or users['username']
            users['money'] = user.money or users['money']
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                return "Sneaker as been updated"
