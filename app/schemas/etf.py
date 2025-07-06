# schemas/etf.py
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from decimal import Decimal

class EtfBase(BaseModel):
    code: str
    name: str
    provider: str
    cost: Decimal

class EtfCreate(EtfBase):
    pass

class EtfUpdate(EtfBase):
    pass

class EtfResponse(EtfBase):
    id: UUID
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True