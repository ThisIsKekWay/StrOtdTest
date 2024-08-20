from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict


class SNewCategory(BaseModel):
    name: str


class SCategory(BaseModel):
    id: int
    name: str

    model_config = SettingsConfigDict(from_attributes=True)
