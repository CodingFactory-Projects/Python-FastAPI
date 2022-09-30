from models.shops import *


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name")
async def say_hello(name: str):
    return {"messages": f"Hello {name}"}
