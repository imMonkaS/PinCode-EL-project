import json
from datetime import datetime

from config.config import APP_DIR


class Database:
    """
    Класс базs данных, по сути просто нужен для объединения базы данных и методов для взаимодействия с ней
    """
    USERS_DATABASE: dict[str, dict[str, any]] = {}

    @staticmethod
    def create_data(**kwargs) -> str:
        new_id = str(int(list(Database.USERS_DATABASE.keys())[-1]) + 1) if len(Database.USERS_DATABASE.keys()) != 0 else '0'
        Database.USERS_DATABASE[new_id] = {}
        for key, value in kwargs.items():
            Database.USERS_DATABASE[new_id][key] = value
        return new_id

    @staticmethod
    def change_data(user_id: str, **kwargs):
        for key, value in kwargs.items():
            Database.USERS_DATABASE[user_id][key] = value

    @staticmethod
    def delete_user(user_id: str):
        Database.USERS_DATABASE.pop(user_id)

    @staticmethod
    def get_user(user_id: str) -> dict[str, any]:
        return Database.USERS_DATABASE[user_id]

    @staticmethod
    def fill_database_with_test_data() -> None:
        """
        Загрузить тестовые данные в бд из заранее заготовленного файла.
        Так как данные берутся с json тут всё в стрингах, в преобразовании смысла пока не вижу.

        Returns:
            None
        """
        with open(f'{APP_DIR}/internal/repositories/db/data/test_data.json', 'r') as file:
            Database.USERS_DATABASE = json.load(file)
        for key in Database.USERS_DATABASE.keys():
            Database.USERS_DATABASE[key]['birth_date'] = datetime.strptime(Database.USERS_DATABASE[key]['birth_date'], "%Y-%m-%d").date()
        print("Data filled successfully")

    @staticmethod
    def save_data_base(filename: str):
        pass

    @staticmethod
    def load_data_base(filename: str):
        pass
