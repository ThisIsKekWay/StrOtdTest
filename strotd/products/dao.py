from sqlalchemy import select

from strotd.dao.base import BaseDAO
from strotd.database import async_session_maker
from strotd.products.models import Products


class ProductsDAO(BaseDAO):
    model = Products

    @classmethod
    async def find_all(cls, page: int = 1, per_page: int = 10, filter: dict = None):
        offset = (page - 1) * per_page
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).offset(offset).limit(per_page)

            if filter:
                if filter.get("name"):
                    query = query.filter(cls.model.name == filter.get("name"))
                if filter.get("category_id"):
                    query = query.filter(cls.model.category_id == filter.get("category_id"))
                if filter.get("price"):
                    query = query.filter(cls.model.price == filter.get("price"))

            result = await session.execute(query)
            return result.mappings().all()
