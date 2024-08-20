from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from strotd.database import Base


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(DECIMAL, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    category = relationship("Categories", back_populates="prod", lazy="subquery")
