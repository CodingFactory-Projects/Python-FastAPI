from pydantic import BaseModel


class Sneakers(BaseModel):
    id: int = None
    img: str
    name: str
    description: str
    colors: str
    price: float
    stock: int


class EditedSneaker(BaseModel):
    img: str = None
    name: str = None
    description: str = None
    colors: str = None
    price: str = None
    stock: str = None
