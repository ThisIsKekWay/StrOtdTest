from sqlalchemy import delete, insert, select, update

from strotd.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, page: int = 1, per_page: int = 10, **filter_by):
        offset = (page - 1) * per_page
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by).offset(offset).limit(per_page)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model.__table__.columns)
            res = await session.execute(query)
            await session.commit()
            return res.mappings().one()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by).returning(cls.model.__table__.columns)
            res = await session.execute(query)
            await session.commit()
            return res.mappings().one()

    @classmethod
    async def update(cls, prod_id, **data):
        async with async_session_maker() as session:
            query = update(cls.model).where(cls.model.id == prod_id).values(**data).returning(cls.model.__table__.columns)
            res = await session.execute(query)
            await session.commit()
            return res.mappings().one()
