from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, get_session
from sqlalchemy.orm import Session
import models
import schemas


def create_refdate1_impl(refdate1: schemas.RefDate1, session: Session = Depends(get_session)):

    # create an instance of the ToDo database model
    dbitem = models.RefDate1(Entity1Id = refdate1.Entity1Id, RefDate = refdate1.RefDate)

    # add it to the session and commit it
    session.add(dbitem)
    session.commit()
    session.refresh(dbitem)

    # return the todo object
    return dbitem