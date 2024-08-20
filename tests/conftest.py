import json

import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy import insert

from strotd.config import settings
from strotd.database import Base, async_session_maker, engine
from strotd.categories.models import Categories
from strotd.products.models import Products
from strotd.main import app as fastapi_app


@pytest.fixture(scope="session", autouse=True)
async def prepare_database():
    assert settings.MODE == "TEST"

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_json(model: str):
        with open(f"tests/mock_{model}.json", "r", encoding="utf-8") as file:
            return json.load(file)

    categories = open_mock_json("cats")
    products = open_mock_json("products")

    async with async_session_maker() as conn:
        for Model, values in [
            (Categories, categories),
            (Products, products),

        ]:
            query = insert(Model).values(values)
            await conn.execute(query)
        await conn.commit()
