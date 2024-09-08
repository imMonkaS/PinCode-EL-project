from config import settings
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.create_db_url())
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    def __repr__(self):
        repr_cols_num = 3
        repr_cols = tuple()

        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in repr_cols or idx < repr_cols_num:
                cols.append(f'{col}={getattr(self, col)}')

        return f'<{self.__class__.__name__} {", ".join(cols)}>'


async def get_async_session():
    async with async_session_maker() as session:
        yield session
