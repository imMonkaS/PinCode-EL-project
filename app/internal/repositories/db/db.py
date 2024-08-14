import json
from datetime import datetime, date

from config.config import APP_DIR
from internal.routers.user.schemas.request.create import CreateProfileRequest


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

    # @classmethod
    # def change_user(
    #         cls,
    #         user_id: str,
    #         login: str = None,
    #         password: str = None,
    #         first_name: str = None,
    #         birth_date: date = None,
    #         last_name: str = None,
    #         middle_name: str = None,
    #         work_experience: int = None,
    # ):
    #     pass

    @classmethod
    def delete_user(cls, user_id: int):
        cls._USERS_DATABASE.pop(user_id)
    
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
        print("Data filled successfully")
