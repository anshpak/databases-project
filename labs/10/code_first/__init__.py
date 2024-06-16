import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import joinedload, contains_eager
from datetime import datetime
from sqlalchemy_utils import database_exists, create_database, drop_database
from typing import List

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('preference_id', Integer, primary_key=True),
                          Column('tea_id', ForeignKey('tea.id'), primary_key=True),
                          Column('consumer_id', ForeignKey('consumers.id'), primary_key=True),
                          Column('rating', Integer, nullable=False))


class Tea(Base):
    __tablename__ = 'tea'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    origin: Mapped[str] = mapped_column(String(30))
    consumers: Mapped[List['Consumer']] = relationship(secondary=association_table, back_populates='tea')


class Consumer(Base):
    __tablename__ = 'consumers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    contact_info: Mapped[str] = mapped_column(String(20))
    tea: Mapped[List['Tea']] = relationship(secondary=association_table, back_populates='consumers')


if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:sic mundus creatus est@localhost/tea")
    if not database_exists(engine.url):
        create_database(engine.url)
    else:
        drop_database(engine.url)
        create_database(engine.url)
    print(database_exists(engine.url))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    cur_session = Session()
