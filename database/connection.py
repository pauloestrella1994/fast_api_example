from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from .settings import settings


engine = create_async_engine(settings.database_url)
async_session = sessionmaker(engine, class_=AsyncSession)
