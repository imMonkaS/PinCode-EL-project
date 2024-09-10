from repositories.user import UserRepository
from schemas.user import (CreateUserSchema, GetUserSchema, ReplaceUserSchema,
                          UpdateUserSchema)


class UserService:
    """ Сервис для работы с пользователем, зависит от репозитория"""

    def __init__(self, user_repo: UserRepository):
        self._user_repo: UserRepository = user_repo

    async def create(
            self,
            data: CreateUserSchema
    ) -> GetUserSchema:
        """
        Создать пользователя по параметрам

        Returns:
            Созданный пользователь
        """
        user = await self._user_repo.create_one(data.model_dump(exclude_none=True))
        user.calculate_age(user.birth_date)

        return user

    async def get_by_id(self, user_id: int) -> GetUserSchema:
        """
        Возвращает информацтю о пользователе по id

        Returns:
            Информация о польозвателе
        """
        user = await self._user_repo.get_by_id(user_id)
        user.calculate_age(user.birth_date)

        return user

    async def get_all(self) -> list[GetUserSchema]:
        users = await self._user_repo.get_all()
        for user in users:
            user.calculate_age(user.birth_date)

        return users

    async def update_by_id(
            self,
            user_id: int,
            data: UpdateUserSchema
    ) -> GetUserSchema:
        """
        Обновить информацию о пользователе по id

        Returns:
            Информация об обновленном пользователе
        """
        user = await self._user_repo.update_by_id(
            user_id,
            data.model_dump(exclude_none=True)
        )
        user.calculate_age(user.birth_date)

        return user

    async def replace_by_id(
            self,
            user_id: int,
            data: ReplaceUserSchema
    ) -> GetUserSchema:
        """
        Заменить информацию о пользователе

        Returns:
            Информация о заменённом пользователе
        """

        user = await self._user_repo.update_by_id(
            user_id,
            data.model_dump()
        )
        user.calculate_age(user.birth_date)

        return user

    async def delete_by_id(self, user_id: int) -> None:
        """
        Удалить пользователя по id
        """

        await self._user_repo.delete_by_id(user_id)
