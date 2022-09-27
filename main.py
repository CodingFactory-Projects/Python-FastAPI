from fastapi import FastAPI

# from typing import Union
from typing import List

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


# print(get_name_with_age("paul", 49))


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


# print(get_items("hello world!", 3481, 452.44, True, b"A"))


def process_items(items: List[str]):
    for item in items:
        print(item)


print(process_items(["hello world!", "hello world2!", "hello world3!"]))

