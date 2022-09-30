from pydantic import BaseModel

from classes.ProductsClass import Products


class Order(BaseModel):
    id_order: int
    products: list[Products] | Products
    total_price: int | None
    client_id: int
