from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# def get_full_name(first_name, last_name):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name
#
#
# print(get_full_name("rui", "gaspar"))
#
#
# def get_full_name(first_name: str, last_name: str):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name
#
#
# print(get_full_name("paul", "walker"))


def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + " is this old: " + str(age)
    return name_with_age


print(get_name_with_age("paul", 49))
