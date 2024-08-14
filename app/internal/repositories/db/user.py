from datetime import date

from fastapi import HTTPException
from internal.repositories.db.db import UserDatabase


class UserRepository:
    """
    Репозирорий для работы с базой данных пользователя
    """

    db = UserDatabase()

    def create_one(
            self,
            login: str,
            password: str,
            first_name: str,
            birth_date: date,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = 0,
    ) -> int:
        """
        Сздать пользователя по параметрам

        Returns:
            id созданного пользователя
        """
        data = {
            'login': login,
            'password': password,
            'first_name': first_name,
            'birth_date': birth_date,
            'last_name': last_name,
            'middle_name': middle_name,
            'work_experience': work_experience
        }
        data = {key: value for key, value in data.items() if value is not None}

        user_id = self.db.create_user(**data)
        return user_id

    def get_one(self, user_id: int) -> dict[str, any]:
        """
        Получить информацию о пользователе по id

        Returns:
            Информацию о пользователе
        """

        try:
            return self.db.get_user(user_id)
        except KeyError:
            raise HTTPException(status_code=404, detail='User does not exist')

    def update(
            self,
            user_id: int,
            login: str = None,
            password: str = None,
            first_name: str = None,
            birth_date: date = None,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = None,
    ) -> int:
        """
        Обновить информацию о пользователи по id

        Returns:
            Количество измененных параметров
        """

        data = {
            'login': login,
            'password': password,
            'first_name': first_name,
            'birth_date': birth_date,
            'last_name': last_name,
            'middle_name': middle_name,
            'work_experience': work_experience
        }
        data = {key: value for key, value in data.items() if value is not None}

        return self.db.update_user(user_id, **data)

    def replace(
            self,
            user_id: int,
            login: str,
            password: str,
            first_name: str,
            birth_date: date,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = 0,
    ) -> int:
        """
        Полностью заменяет информацию о пользователе.

        Returns:
            id по которому заменили пользователя
        """

        data = {
            'login': login,
            'password': password,
            'first_name': first_name,
            'birth_date': birth_date,
            'last_name': last_name,
            'middle_name': middle_name,
            'work_experience': work_experience
        }
        data = {key: value for key, value in data.items() if value is not None}

        return self.db.replace_user(user_id, **data)

    def delete(self, user_id: int) -> int:
        """
        Удаление пользователя по id

        Returns:
            id пользователя, которого удалили
        """

        try:
            return self.db.delete_user(user_id)
        except KeyError:
            raise HTTPException(status_code=404, detail='User does not exist')
