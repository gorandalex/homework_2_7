from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique = True, nullable=False)
    
    students = relationship('Student', back_populates='group')

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False) 
    
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    group_id = Column('group_id', ForeignKey(Group.id, ondelete='CASCADE'), nullable=False)
    
    group = relationship(Group, back_populates = 'students')   