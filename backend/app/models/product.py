from sqlalchemy import Column, Integer, String

from app.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
    unit = Column(String, nullable=False)
    price = Column(Integer, nullable=False)