"""SQLAlchemy database session management."""
from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from ..core.config import settings


class Base(DeclarativeBase):
    pass


def get_engine():
    return create_async_engine(settings.DATABASE_URL, echo=False, future=True)


def get_sessionmaker() -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(bind=get_engine(), expire_on_commit=False)


async_session = get_sessionmaker()


async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session
