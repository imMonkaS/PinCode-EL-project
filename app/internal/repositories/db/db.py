import json
from datetime import date

from config.config import APP_DIR
from internal.routers.user.schemas.request.create import CreateProfileRequest
from internal.routers.user.schemas.request.update import UpdateUserRequest


class UserDatabase:
    """
    Класс базs данных
    """
    _counter: int = 0
    _USERS_DATABASE: dict[int, dict[str, any]] = {}

    @classmethod
    def create_user(
            cls,
            login: str,
            password: str,
            first_name: str,
            birth_date: date,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = 0,
    ) -> int:
        new_id = cls._counter
        cls._counter += 1

        model = CreateProfileRequest(
            login=login,
            password=password,
            first_name=first_name,
            birth_date=birth_date,
            last_name=last_name,
            middle_name=middle_name,
            work_experience=work_experience
        )

        cls._USERS_DATABASE[new_id] = model.model_dump()
        return new_id

    @classmethod
    def get_user(cls, user_id: int) -> dict[str, any]:
        return cls._USERS_DATABASE[user_id]

    @classmethod
    def replace_user(
            cls,
            user_id: int,
            login: str,
            password: str,
            first_name: str,
            birth_date: date,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = 0,
    ) -> int:
        model = CreateProfileRequest(
            login=login,
            password=password,
            first_name=first_name,
            birth_date=birth_date,
            last_name=last_name,
            middle_name=middle_name,
            work_experience=work_experience
        )

        cls._USERS_DATABASE[user_id] = model.model_dump()
        return user_id

    @classmethod
    def update_user(
            cls,
            user_id: int,
            login: str = None,
            password: str = None,
            first_name: str = None,
            birth_date: date = None,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = None,
    ) -> int:
        tmp_model = UpdateUserRequest.model_validate(cls._USERS_DATABASE[user_id])
        changes_counter = 0
        if login:
            tmp_model.login = login
            changes_counter += 1

        if password:
            tmp_model.password = password
            changes_counter += 1

        if first_name:
            tmp_model.first_name = first_name
            changes_counter += 1

        if birth_date:
            tmp_model.birth_date = birth_date
            changes_counter += 1

        if last_name:
            tmp_model.last_name = last_name
            changes_counter += 1

        if middle_name:
            tmp_model.middle_name = middle_name
            changes_counter += 1

        if work_experience:
            tmp_model.work_experience = work_experience
            changes_counter += 1
        cls._USERS_DATABASE[user_id] = tmp_model.model_dump()
        return changes_counter

    @classmethod
    def delete_user(cls, user_id: int) -> int:
        cls._USERS_DATABASE.pop(user_id)
        return user_id

    @classmethod
    def fill_database_with_test_data(cls) -> None:
        """
        Загрузить тестовые данные в бд из заранее заготовленного файла.
        Так как данные берутся с json тут всё в стрингах, в преобразовании смысла пока не вижу.

        Returns:
            None
        """
        with open(f'{APP_DIR}/internal/repositories/db/data/test_data.json', 'r') as file:
            test_data = json.load(file)
        for key in test_data.keys():
            cls._counter += 1

            model = CreateProfileRequest(**test_data[key])
            cls._USERS_DATABASE[int(key)] = model.model_dump()
