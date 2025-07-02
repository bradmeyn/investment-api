from fastapi import APIRouter

etf_router = APIRouter(prefix="/etfs", tags=["etfs"])


etfs = [
    {"id": "1", "name": "ETF 1", "description": "Description of ETF 1"},
    {"id": "2", "name": "ETF 2", "description": "Description of ETF 2"},
    {"id": "3", "name": "ETF 3", "description": "Description of ETF 3"},
]

@etf_router.get("/")
async def get_etfs():
    return {"etfs": etfs}   


@etf_router.get("/{etf_id}")
async def get_etf(etf_id: str):
    return {"message": f"ETF {etf_id}"}

@etf_router.post("/")
async def create_etf(etf: dict):
    return {"message": "ETF created", "etf": etf}

@etf_router.put("/{etf_id}")
async def update_etf(etf_id: str, etf: dict):
    return {"message": f"ETF {etf_id} updated", "etf": etf}

@etf_router.delete("/{etf_id}")
async def delete_etf(etf_id: str):
    return {"message": f"ETF {etf_id} deleted"}
