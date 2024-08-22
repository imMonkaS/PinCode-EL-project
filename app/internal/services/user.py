from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from internal.models.user import GetUserModel
from internal.repositories.db.user import UserRepository


class UserService:
    """ Сервис для работы с пользователем, зависит от репозитория"""

    def __init__(self, user_repo: UserRepository):
        self._user_repository = user_repo

    def create(
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
        Создать пользователя по параметрам

        Returns:
            id созданного пользователя
        """
        user_id = self._user_repository.create_one(
            login=login,
            password=password,
            first_name=first_name,
            birth_date=birth_date,
            last_name=last_name,
            middle_name=middle_name,
            work_experience=work_experience
        )
        return user_id

    def get_by_id(self, user_id: int) -> GetUserModel:
        """
        Возвращает информацтю о пользователе по id

        Returns:
            Информация о польозвателе, валидируется с помощью pydantic
        """
        user_data = self._user_repository.get_one(user_id).copy()

        user_data.pop('password')
        user_data['age'] = relativedelta(datetime.today(), user_data['birth_date']).years
        return GetUserModel.model_validate(user_data)

    def update_by_id(
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
        Обновить информацию о пользователе по id

        Returns:
            Количество обновленных параметров
        """

        return self._user_repository.update(
            user_id,
            login=login,
            password=password,
            first_name=first_name,
            birth_date=birth_date,
            last_name=last_name,
            middle_name=middle_name,
            work_experience=work_experience
        )

    def replace_by_id(
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
        Заменить информацию о пользователе

        Returns:
            id пользователя, которого заменили
        """

        return self._user_repository.replace(
            user_id,
            login=login,
            password=password,
            first_name=first_name,
            birth_date=birth_date,
            last_name=last_name,
            middle_name=middle_name,
            work_experience=work_experience
        )

    def delete_by_id(self, user_id: int):
        """
        Удалить пользователя по id

        Returns:
            id пользователя, которого удалили
        """

        return self._user_repository.delete(user_id)
