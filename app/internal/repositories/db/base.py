from abc import ABC, abstractmethod

from internal.core.exceptions import (IntegrityException, ProgrammingException,
                                      UserDoesNotExistException)
from internal.schemas.user import GetUserSchema
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError, NoResultFound, ProgrammingError
from sqlalchemy.ext.asyncio import AsyncSession


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

    def __init__(self, session: AsyncSession):
        self.session = session

    model = None

    async def create_one(self, data: dict) -> GetUserSchema:
        stmt = insert(self.model).values(**data).returning(self.model)
        try:
            res = await self.session.execute(stmt)
            await self.session.commit()
            return res.scalar_one().to_read_model()
        except IntegrityError as e:
            raise IntegrityException from e

    async def get_by_id(self, item_id: int) -> GetUserSchema:
        stmt = select(self.model).filter_by(id=item_id)
        try:
            res = await self.session.execute(stmt)
            return res.scalar_one().to_read_model()
        except NoResultFound as e:
            raise UserDoesNotExistException from e

    async def get_all(self) -> list[GetUserSchema]:
        stmt = select(self.model)
        res = await self.session.execute(stmt)
        res = [row[0].to_read_model() for row in res.all()]
        return res

    async def update_by_id(self, item_id: int, data: dict) -> GetUserSchema:
        stmt = update(self.model).values(**data).filter_by(id=item_id).returning(self.model)
        try:
            res = await self.session.execute(stmt)
            await self.session.commit()

            return res.scalar_one().to_read_model()
        except NoResultFound as e:
            raise UserDoesNotExistException from e
        except IntegrityError as e:
            raise IntegrityException from e
        except ProgrammingError as e:
            raise ProgrammingException from e

    async def delete_by_id(self, item_id: int) -> None:
        stmt = delete(self.model).filter_by(id=item_id)
        await self.session.execute(stmt)
        await self.session.commit()
