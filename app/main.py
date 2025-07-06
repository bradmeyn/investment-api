
from fastapi import FastAPI
from .routers.etfs import etf_router
from .database import engine, Base
from .config import settings


print("Starting application...")
print(f"Settings: {settings}")
print(f"Database URL: {settings.database_url}")


if not settings.database_url:
    raise ValueError("DATABASE_URL environment variable is not set.")
# Debug: Print the database URL
print(f"Using database URL: {settings.database_url}")   

# Create tables when app starts
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(etf_router)