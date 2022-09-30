from pydantic import BaseModel


class Products(BaseModel):
    product_id: int
    price: float
    quantity: int
