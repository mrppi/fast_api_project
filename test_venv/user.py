from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "training"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    email = Column(String(100))
    age = Column(Integer)  


class Student(Base):
    __tablename__="student"
    __table_arg__={"schema:training"}
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(50))
    