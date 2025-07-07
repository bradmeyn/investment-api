# models/etf.py
from sqlalchemy import String, DateTime, Uuid, DECIMAL
from sqlalchemy.orm import mapped_column, Mapped
from ..database import Base  
import uuid
import datetime

class Etf(Base):
    __tablename__ = "etfs"

    id: Mapped[Uuid] = mapped_column(
        Uuid(),
        default=uuid.uuid4,
        primary_key=True,
        unique=True,
        nullable=False
    )
    code: Mapped[str] = mapped_column(
        String(10),
        unique=True,
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    provider: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    cost: Mapped[float] = mapped_column(
        DECIMAL(precision=5, scale=2),
        nullable=False
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.datetime.now,
        nullable=False
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.datetime.now,
        onupdate=datetime.datetime.now,
        nullable=False
    )