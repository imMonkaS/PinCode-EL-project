import json
from datetime import date

from config.config import APP_DIR
from internal.routers.user.schemas.request import (CreateProfileRequest,
                                                   UpdateUserRequest)


class UserDatabase:
    """
    Класс базs данных пользователя с авто-инкриментом, id - PK. По сути имитация настоящей бд.
    Выполняет CRUD-операции. Все операции, а также считывание тестовых данных валидируется при помощи pydantic
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
        """
        Добавить пользователя в бд.

        Returns:
            id созданного пользователя
        """

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
        """
        По id пользователя возвращает информацию о нем

        Returns:
            Информация о пользователе
        """

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
        """
        Полностью заменяет информацию о пользователе по id

        Returns:
            id по которому заменили пользователя
        """

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
        """
        Обновить выборочные поля информации о пользователе.

        Returns:
            Количество измененных полей.
        """
        new_data = {
            'login': login,
            'password': password,
            'first_name': first_name,
            'birth_date': birth_date,
            'last_name': last_name,
            'middle_name': middle_name,
            'work_experience': work_experience
        }
        new_data = {key: value for key, value in new_data.items() if value is not None}

        model = UpdateUserRequest.model_validate(cls._USERS_DATABASE[user_id])
        new_model = model.model_copy(update=new_data)

        cls._USERS_DATABASE[user_id] = new_model.model_dump()

        return len(new_data.values())

    @classmethod
    def delete_user(cls, user_id: int) -> int:
        """
        Удаляет пользователя из базы данных по id

        Returns:
            id который был у удаленного пользователя
        """

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
