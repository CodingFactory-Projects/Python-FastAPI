from models.sneakers import *


@app.get("/")
async def root():
    return {"message": "Hello World"}


# return json from data.json
@app.get("/data")
async def get_data():
    return data
