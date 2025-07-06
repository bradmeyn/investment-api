from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from ..database import get_db 
from ..models.etf import Etf


etf_router = APIRouter(prefix="/etfs", tags=["etfs"])


etfs = [
    {"id": "1", "name": "ETF 1", "description": "Description of ETF 1"},
    {"id": "2", "name": "ETF 2", "description": "Description of ETF 2"},
    {"id": "3", "name": "ETF 3", "description": "Description of ETF 3"},
]

@etf_router.get("/")
async def get_etfs(db: Session = Depends(get_db)):
    return db.query(Etf).all() 

@etf_router.get("/{etf_id}")
async def get_etf(etf_id: str, db: Session = Depends(get_db)):
    etf = db.query(Etf).filter(Etf.id == etf_id).first()
    if not etf:
        return {"message": f"ETF {etf_id} not found"}
    return etf

@etf_router.post("/")
async def create_etf(etf: dict, db: Session = Depends(get_db)):
    return {"message": "ETF created", "etf": etf}

@etf_router.put("/{etf_id}")
async def update_etf(etf_id: str, etf: dict, db: Session = Depends(get_db)):
    return {"message": f"ETF {etf_id} updated", "etf": etf}

@etf_router.delete("/{etf_id}")
async def delete_etf(etf_id: str, db: Session = Depends(get_db)):
    return {"message": f"ETF {etf_id} deleted"}
