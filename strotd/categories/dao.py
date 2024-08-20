from sqlalchemy import select

from strotd.dao.base import BaseDAO
from strotd.categories.models import Categories
from strotd.database import async_session_maker


class CategoryDAO(BaseDAO):
    model = Categories
