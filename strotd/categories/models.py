from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from strotd.database import Base


class Categories(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)

    prod = relationship("Products", back_populates="category", lazy="subquery")
