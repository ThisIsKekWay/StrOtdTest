from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class SNewProduct(BaseModel):
    name: str
    description: str
    price: Decimal
    category_id: int


class SProduct(BaseModel):
    id: int
    name: str
    description: str
    price: Decimal
    category_id: int

    model_config = SettingsConfigDict(from_attributes=True)


class SProductFilter(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[Decimal] = None

    model_config = SettingsConfigDict(from_attributes=True)
