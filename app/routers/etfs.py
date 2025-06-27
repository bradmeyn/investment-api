from fastapi import APIRouter

etf_router = APIRouter(prefix="/etfs", tags=["etfs"])

@etf_router.get("/")
async def get_etfs():
    return {"message": "Hello World"}


@etf_router.get("/{etf_id}")
async def get_etf(etf_id: str):
    return {"message": f"ETF {etf_id}"}

@etf_router.post("/")
async def create_etf(etf: dict):
    return {"message": "ETF created", "etf": etf}

@etf_router.put("/{etf_id}")
async def update_etf(etf_id: str, etf: dict):
    return {"message": f"ETF {etf_id} updated", "etf": etf}




