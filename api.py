from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
import pydantic
from database import Base, engine, get_session
from sqlalchemy.orm import Session
import models
import schemas


def session_commit(dbitem: pydantic.BaseModel, session: Session = Depends(get_session)):
    # add the database model to the session and commit it
    session.add(dbitem)
    session.commit()
    session.refresh(dbitem)

def create_refdate1_impl(refdate1: schemas.RefDate1, session: Session = Depends(get_session)):
    # create an instance of the database model
    dbitem = models.RefDate1(**refdate1.__dict__)
    # add it to the session and commit it
    session_commit(dbitem, session)
    # return the todo object
    return dbitem

def create_refdate2_impl(refdate2: schemas.RefDate2, session: Session = Depends(get_session)):
    # create an instance of the database model
    dbitem = models.RefDate2(**refdate2.__dict__)
    # add it to the session and commit it
    session_commit(dbitem, session)
    # return the todo object
    return dbitem

def create_refdate3_impl(refdate3: schemas.RefDate3, session: Session = Depends(get_session)):
    # create an instance of the database model
    dbitem = models.RefDate3(**refdate3.__dict__)
    # add it to the session and commit it
    session_commit(dbitem, session)
    # return the todo object
    return dbitem
