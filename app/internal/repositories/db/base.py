from abc import ABC, abstractmethod

from internal.repositories.db.helpers import async_session_maker
from internal.schemas.user import GetUserSchema
from sqlalchemy import delete, insert, select, update


class AbstractRepository(ABC):
    """
    Абстрактный класс репозитория
    """
    @abstractmethod
    async def create_one(self, *args, **kwargs):
        pass

    @abstractmethod
    async def get_by_id(self, *args, **kwargs):
        pass

    @abstractmethod
    async def update_by_id(self, *args, **kwargs):
        pass

    @abstractmethod
    async def delete_by_id(self, *args, **kwargs):
        pass


class SQLAlchemyRepository(AbstractRepository):
    """
    Базовый класс репозитория для взаимодействия с бд
    """

    model = None

    async def create_one(self, data: dict) -> GetUserSchema:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one().to_read_model()

    async def get_by_id(self, item_id: int) -> GetUserSchema:
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(id=item_id)
            res = await session.execute(stmt)
            return res.scalar_one().to_read_model()

    async def get_all(self) -> list[GetUserSchema]:
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.execute(stmt)
            res = [row[0].to_read_model() for row in res.all()]
            return res

    async def update_by_id(self, item_id: int, data: dict) -> GetUserSchema:
        async with async_session_maker() as session:
            stmt = update(self.model).values(**data).filter_by(id=item_id).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()

            return res.scalar_one().to_read_model()

    async def delete_by_id(self, item_id: int) -> None:
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(id=item_id)
            await session.execute(stmt)
            await session.commit()
