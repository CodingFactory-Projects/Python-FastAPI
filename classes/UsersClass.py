from pydantic import BaseModel




class User(BaseModel): # Create an object which will be used to validate the data and modified
    id: int
    username: str | None = None
    money: int | None = None
