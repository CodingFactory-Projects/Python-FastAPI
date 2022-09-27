from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def load_data():
    with open('data.json') as f:
        return json.load(f)


json_data = load_data()
user_list = []


@app.get("/users/")
async def get_users():
    for user in json_data['users']:
        if user not in user_list:
            user_list.append(user)
    return user_list
