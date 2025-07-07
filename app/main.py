from fastapi import FastAPI
from .routers.etfs import etf_router
from .database import engine, Base
from .config import settings

# Import all models here so Base knows about them
from .models.etf import Etf  # This is important!

if not settings.database_url:
    raise ValueError("DATABASE_URL environment variable is not set.")

# Create tables when app starts
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Investment API", version="1.0.0")
app.include_router(etf_router)

@app.get("/")
async def root():
    return {"message": "Investment API is running"}