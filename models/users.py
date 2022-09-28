from fastapi import FastAPI
import json

app = FastAPI()


def load_data():
    with open('data.json') as f:
        return json.load(f)


json_data = load_data()


@app.get("/users/")
async def get_users():
    return json_data['users']


@app.get("/users/{user_id}")
async def create_user(user_id: int):
    for user in json_data['users']:
        if user_id == user['id']:
            return user
        else:
            return {"No such id in this table"}