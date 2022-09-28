from fastapi import FastAPI
import json
from pydantic import BaseModel

app = FastAPI()


def load_data():
    with open('data.json') as f:
        return json.load(f)


data = load_data()


@app.get("/users/")
async def get_users():
    return data['users']


@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    for user in data['users']:
        if user_id == user['id']:
            return user


class User(BaseModel):
    id: int
    username: str
    money: int | None = None


@app.post("/users/")
async def create_user(user: User):
    with open('data.json', mode='w') as f:
        data['users'].append(user.dict())
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))
    return 'user'


@app.delete("/users/{user_id}")
async def delete_users(user_id: int):
    for user in data['users']:
        if user_id == user['id']:
            data['users'].remove(user)
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                print(data)
            return data
