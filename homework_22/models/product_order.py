from sqlalchemy import Column
from sqlalchemy import INTEGER, VARCHAR, FLOAT
from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(50), unique=True)
    price = Column(FLOAT)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}'


class Order(Base):
    __tablename__ = "orders"

    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey("products.id"), nullable=False)
    quantity = Column(INTEGER)

    def __str__(self):
        return f'id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity}'
