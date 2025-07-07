from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db 
from ..models.etf import Etf
from ..schemas.etf import EtfCreate, EtfUpdate, EtfResponse
from typing import List

etf_router = APIRouter(prefix="/etfs", tags=["etfs"])

@etf_router.get("/", response_model=List[EtfResponse])
async def get_etfs(db: Session = Depends(get_db)):
    return db.query(Etf).all()

@etf_router.get("/{etf_code}", response_model=EtfResponse)
async def get_etf(etf_code: str, db: Session = Depends(get_db)):
    etf = db.query(Etf).filter(Etf.code == etf_code).first()
    if not etf:
        raise HTTPException(status_code=404, detail=f"ETF {etf_code} not found")
    return etf

@etf_router.post("/", response_model=EtfResponse)
async def create_etf(etf: EtfCreate, db: Session = Depends(get_db)):
    new_etf = Etf(**etf.model_dump())
    db.add(new_etf)
    db.commit()
    db.refresh(new_etf)  # Get the created record with id, timestamps
    return new_etf

@etf_router.put("/{etf_code}", response_model=EtfResponse)
async def update_etf(etf_code: str, etf: EtfUpdate, db: Session = Depends(get_db)):
    db_etf = db.query(Etf).filter(Etf.code == etf_code).first()
    if not db_etf:
        raise HTTPException(status_code=404, detail=f"ETF {etf_code} not found")
    
    for key, value in etf.model_dump().items():
        setattr(db_etf, key, value)
    
    db.commit()
    db.refresh(db_etf)
    return db_etf

@etf_router.delete("/{etf_code}")
async def delete_etf(etf_code: str, db: Session = Depends(get_db)):
    db_etf = db.query(Etf).filter(Etf.code == etf_code).first()
    if not db_etf:
        raise HTTPException(status_code=404, detail=f"ETF {etf_code} not found")
    
    db.delete(db_etf)
    db.commit()
    return {"message": f"ETF {etf_code} deleted"}