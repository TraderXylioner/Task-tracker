from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import settings

engine = create_async_engine(
    url=settings.Database.URL,
    echo=False,
)
session = sessionmaker(engine, class_=AsyncSession)


async def get_session():
    try:
        session_object: AsyncSession = session()
        yield session_object
    finally:
        await session_object.close()
