from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Pythonbanking
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/api/v1/pythonbanking", tags=["pythonbanking"])

class PythonbankingCreate(BaseModel):
    name: str
    description: Optional[str] = None

class PythonbankingResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    
    class Config:
        orm_mode = True

@router.get("/", response_model=List[PythonbankingResponse])
def get_all_pythonbanking(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(Pythonbanking).offset(skip).limit(limit).all()
    return items

@router.get("/{item_id}", response_model=PythonbankingResponse)
def get_pythonbanking_by_id(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Pythonbanking).filter(Pythonbanking.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Pythonbanking not found")
    return item

@router.post("/", response_model=PythonbankingResponse)
def create_pythonbanking(item: PythonbankingCreate, db: Session = Depends(get_db)):
    db_item = Pythonbanking(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item