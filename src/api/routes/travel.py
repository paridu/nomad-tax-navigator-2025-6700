from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.database.session import get_db
from src.database import models
from src.api.schemas.user import TravelEntryCreate

router = APIRouter()

@router.post("/{user_id}/log", response_model=TravelEntryCreate)
def log_travel(user_id: int, entry: TravelEntryCreate, db: Session = Depends(get_db)):
    db_entry = models.TravelEntry(**entry.dict(), user_id=user_id)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry

@router.get("/{user_id}/history")
def get_travel_history(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.TravelEntry).filter(models.TravelEntry.user_id == user_id).all()