from fastapi import FastAPI

from methodes.sneakers import *
from methodes.orders import *
from methodes.shops import *
from methodes.users import *


# app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Write in the path /docs to see the documentation"}
