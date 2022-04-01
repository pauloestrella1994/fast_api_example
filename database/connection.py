from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .settings import settings


engine = create_async_engine(settings.database_url)
async_session = sessionmaker(engine, class_=AsyncSession)

engine_sync = create_engine(settings.database_url_sync)
SessionLocal = sessionmaker(bind=engine_sync)
