from fastapi import FastAPI
from routers.etfs import etf_router

app = FastAPI()

# /etfs 
app.include_router(etf_router)