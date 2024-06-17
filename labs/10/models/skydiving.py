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


# class EmployeePosition(enum.Enum):
#     SKYDIVING_INSTRUCTOR = 'skydiving-instructor'
#     SAFETY_INSTRUCTOR = 'safety-instructor'
#     TRAINER = 'trainer'
#     MANAGER = 'manager'
#     MECHANIC = 'mechanic'
#     PYLOT = 'pylot'


# Classes Employee and contracts described in a new notation with one-to-one relationship.
class Employee(Base):
    __tablename__ = 'employees'
    id: Mapped[int] = mapped_column('employee_id', primary_key=True)
    name: Mapped[str] = mapped_column('employee_name', nullable=False)
    surname: Mapped[str] = mapped_column('employee_surname', nullable=False)
    position: Mapped[str] = mapped_column('employee_position', nullable=False)
    contact_info: Mapped[str] = mapped_column('contact_info', nullable=False)
    photo: Mapped[str] = mapped_column('employee_photo')
    contract: Mapped['Contract'] = relationship(back_populates='employee', cascade='delete, save-update')

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "position": self.position,
            "contact_info": self.contact_info,
            "photo": self.photo
        }

    def __repr__(self):
        return ("<Employee(id ='%s', name='%s', surname='%s', position='%s', info='%s', photo='%s')>" %
                (self.id, self.name, self.surname, self.position, self.contact_info, self.photo))


class Contract(Base):
    __tablename__ = 'contracts'
    id: Mapped[int] = mapped_column('contract_id', ForeignKey('employees.employee_id'), primary_key=True)
    start_date: Mapped[datetime] = mapped_column('contract_start_date', nullable=False)
    end_date: Mapped[datetime] = mapped_column('contract_end_date', nullable=False)
    salary: Mapped[float] = mapped_column('employee_salary', nullable=False)
    employee: Mapped['Employee'] = relationship(back_populates='contract')

    def __repr__(self):
        return ("<Contract(id ='%s', start_date='%s', end_date='%s', salary='%s')>" % (self.id, self.start_date,
                                                                                       self.end_date, self.salary))


# Classes to check the work of adding new rows.
class Parent(Base):
    __tablename__ = 'parents'
    id: Mapped[int] = mapped_column('parent_id', primary_key=True)
    name: Mapped[str] = mapped_column('parent_name', nullable=False)
    child: Mapped['Child'] = relationship(back_populates='parent', cascade='delete, save-update')
    deceases: Mapped[List['Decease']] = relationship(back_populates='parent', cascade='delete, save-update')
    cards: Mapped[List['Card']] = relationship(back_populates='parent', cascade='delete, save-update')

    def __repr__(self):
        return "<Parent(id ='%s', name='%s')>" % (self.id, self.name)


# One-to-one connection.
class Child(Base):
    __tablename__ = 'children'
    id: Mapped[int] = mapped_column('child_id', ForeignKey('parents.parent_id'), primary_key=True)
    name: Mapped[str] = mapped_column('child_name', nullable=False)
    parent: Mapped['Parent'] = relationship(back_populates='child')

    def __repr__(self):
        return "<Child(id ='%s', name='%s')>" % (self.id, self.name)


# One-to-many connection.
class Decease(Base):
    __tablename__ = 'deceases'
    decease_id: Mapped[int] = mapped_column('decease_id', primary_key=True)
    id: Mapped[int] = mapped_column('parent_id', ForeignKey('parents.parent_id'))
    name: Mapped[str] = mapped_column('decease_name', nullable=False)
    parent: Mapped['Parent'] = relationship(back_populates='deceases')

    def __repr__(self):
        return "<Decease(decease_id ='%s', id = '%s', name='%s')>" % (self.decease_id, self.id, self.name)


class Doctor(Base):
    __tablename__ = 'doctors'
    id: Mapped[int] = mapped_column('doctor_id', primary_key=True)
    name: Mapped[str] = mapped_column('doctor_name', nullable=False)
    cards: Mapped[List['Card']] = relationship(back_populates='doctor', cascade='delete, save-update')

    def __repr__(self):
        return "<Doctor(id = '%s', name = '%s'>)" % (self.id, self.name)


class Card(Base):
    __tablename__ = 'cards'
    doctor_id: Mapped[int] = mapped_column('doctor_id', ForeignKey('doctors.doctor_id'), primary_key=True)
    parent_id: Mapped[int] = mapped_column('parent_id', ForeignKey('parents.parent_id'), primary_key=True)
    doctor: Mapped['Doctor'] = relationship(back_populates='cards')
    parent: Mapped['Parent'] = relationship(back_populates='cards')

    def __repr__(self):
        return "<Card(doctor_id = '%s', parent_id = '%s')>" % (self.doctor_id, self.parent_id)
