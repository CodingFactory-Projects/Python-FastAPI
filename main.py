from fastapi import FastAPI

# from typing import Union
from typing import List, Optional

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


# print(process_items(["hello world!", "hello world2!", "hello world3!"]))


def process_items2(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


# print(process_items2((1, 2, "hello world!"), {b"hello", b"world"}))


def process_items3(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# print(process_items3({"banana": 4, "apple": 2, "orange": 1.5}))


def process_item(item: int | str):
    print(item)


# process_item("hello world!")


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# say_hi("Rui")


def say_hi2(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# say_hi2()


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


# print(get_person_name(Person("Rui")))
