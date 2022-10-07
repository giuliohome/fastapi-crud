import datetime
from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class ToDoCreate(BaseModel):
    task: str

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    task: str

    class Config:
        orm_mode = True

class RefDate1(BaseModel):
    Entity1Id: int
    RefDate: datetime.date

    class Config:
        orm_mode = True

class RefDate2(BaseModel):
    Entity2Id: int
    RefDate: datetime.date

    class Config:
        orm_mode = True

class RefDate3(BaseModel):
    Entity3Id: int
    RefDate: datetime.date

    class Config:
        orm_mode = True
