import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import joinedload, contains_eager
from datetime import datetime
# from sqlalchemy_utils import database_exists, create_database, drop_database
from typing import List


Base = declarative_base()
customer_product_table = Table('customer_product', Base.metadata,
                            Column('product_id', ForeignKey('product_id'), primary_key=True),
                            Column('customer_id', ForeignKey('customer_id'), primary_key=True))
profile = Table('profile', Base.metadata,
                Column('profile_id', ForeignKey('profile_id'), primary_key=True))



class Product(Base):
    __table_name__ = 'products'
    product_id: Mapped[int] = mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(30))
    product_price: Mapped[int] = mapped_column()
    customers: Mapped[List['Customer']] = relationship(secondary=customer_product_table, back_populates='products')

class Customer(Base):
    __table_name__ = 'customers'
    customer_id: Mapped[int] = mapped_column(primary_key=True)
    customer_name: Mapped[str] = mapped_column(String(30))
    customer_surname: Mapped[str] = mapped_column(String(30))
    products: Mapped[List['Product']] = relationship(secondary=customer_product_table, back_populates='customers')

class Profile(Base):
    __table_name__ = 'profiles'
    profile_id: Mapped[int] = mapped_column(primary_key=True)
    profile_nickname: Mapped[str] = mapped_column(String(30))
    customers: Mapped[List['Customer']] = relationship(secondary=profile, back_populates='customers')

if __name__ == '__main__':
    # Вариант 12

