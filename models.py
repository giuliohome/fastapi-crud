from sqlalchemy import Column, Integer, String, Date
from database import Base

# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))

class RefDate1(Base):
    __tablename__ = 'refdate1'
    Entity1Id = Column(Integer, primary_key=True)
    RefDate = Column(Date)

class RefDate2(Base):
    __tablename__ = 'refdate2'
    Entity2Id = Column(Integer, primary_key=True)
    RefDate = Column(Date)

class RefDate3(Base):
    __tablename__ = 'refdate3'
    Entity3Id = Column(Integer, primary_key=True)
    RefDate = Column(Date)
