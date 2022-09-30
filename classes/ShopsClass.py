from pydantic import BaseModel
from typing import Optional


class shops(BaseModel):
    shop_id: int
    country: str
    city: str
    adress: str
    owner: str
    loyer: Optional[float] = None
