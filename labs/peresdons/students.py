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


class MaleStud(Base):
    __tablename__ = 'male_students'
    id: Mapped[int] = mapped_column('male_student_id', primary_key=True)
    name: Mapped[str] = mapped_column('male_student_name', nullable=False)
    surname: Mapped[str] = mapped_column('male_student_surname', nullable=False)
    group: Mapped[int] = mapped_column('male_student_group', nullable=False)
    course: Mapped[int] = mapped_column('male_student_course', nullable=False)
    birth_date: Mapped[datetime] = mapped_column('male_student_birthdate', nullable=False)
    military_service: Mapped['MilitaryService'] = relationship(back_populates='male_student', cascade='delete, '
                                                                                                      'save-update')
    friends: Mapped[List['Friendship']] = relationship(back_populates='male_student', cascade='delete, save-update')

    def __repr__(self):
        return ("<Male student(id = '%s', name = '%s'>, surname = '%s', group = '%s', course = '%s', birth_date = "
                "'%s')") % (self.id, self.name, self.surname, self.group, self.course, self.birth_date)


# One-to-one connection.
class MilitaryService(Base):
    __tablename__ = 'military_service'
    id: Mapped[int] = mapped_column('military_service_id', ForeignKey('male_students.male_student_id'), primary_key=True)
    rank: Mapped[str] = mapped_column('military_rank', nullable=False)
    male_student: Mapped['MaleStud'] = relationship(back_populates='military_service')

    def __repr__(self):
        return "<Military service(id ='%s', rank='%s')>" % (self.id, self.rank)


#
# # One-to-many connection.
class Child(Base):
    __tablename__ = 'children'
    child_id: Mapped[int] = mapped_column('child_id', primary_key=True)
    parent_id: Mapped[int] = mapped_column('parent_id', ForeignKey('female_students.female_student_id'))
    name: Mapped[str] = mapped_column('child_name', nullable=False)
    female_student: Mapped['FemaleStud'] = relationship(back_populates='children')

    def __repr__(self):
        return "<Child(child_id ='%s', parent_id = '%s', name='%s')>" % (self.child_id, self.parent_id, self.name)


class FemaleStud(Base):
    __tablename__ = 'female_students'
    id: Mapped[int] = mapped_column('female_student_id', primary_key=True)
    name: Mapped[str] = mapped_column('female_student_name', nullable=False)
    surname: Mapped[str] = mapped_column('female_student_surname', nullable=False)
    group: Mapped[int] = mapped_column('female_student_group', nullable=False)
    course: Mapped[int] = mapped_column('female_student_course', nullable=False)
    birth_date: Mapped[datetime] = mapped_column('female_student_date_of_birth', nullable=False)
    children: Mapped[List['Child']] = relationship(back_populates='female_student', cascade='delete, save-update')
    friends: Mapped[List['Friendship']] = relationship(back_populates='female_student', cascade='delete, save-update')

    def __repr__(self):
        return ("<Female student(id = '%s', name = '%s'>, surname = '%s', group = '%s', course = '%s', birth_date = "
                "'%s')") % (self.id, self.name, self.surname, self.group, self.course, self.birth_date)


class Friendship(Base):
    __tablename__ = 'cards'
    friendship_id: Mapped[int] = mapped_column('friendship_id', primary_key=True)
    male_student_id: Mapped[int] = mapped_column('male_student_id', ForeignKey('male_students.male_student_id'))
    female_student_id: Mapped[int] = mapped_column('female_student_id', ForeignKey('female_students.female_student_id'))
    male_student: Mapped['MaleStud'] = relationship(back_populates='friends')
    female_student: Mapped['FemaleStud'] = relationship(back_populates='friends')

    def __repr__(self):
        return "<Friendship(friendship_id = '%s', male_student_id = '%s', female_student_id = '%s')>" % (self.friendship_id, self.male_student_id, self.female_student_id)
