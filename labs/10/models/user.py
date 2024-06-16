import enum
from sqlalchemy import Enum
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum, LargeBinary, Date, Numeric
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.orm import joinedload, contains_eager
from datetime import datetime
from sqlalchemy import select
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

Base = declarative_base()

class User(Base):
    __tablename__ = 'users_info'
    login: Mapped[str] = mapped_column('user_login', primary_key=True)
    password: Mapped[str] = mapped_column('user_password', nullable=False)
    role: Mapped[str] = mapped_column('user_role', nullable=False)