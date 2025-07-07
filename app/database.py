from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


if not settings.database_url:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # Base class for all models

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()