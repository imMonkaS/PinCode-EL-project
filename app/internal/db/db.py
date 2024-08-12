import json

from config.config import APP_DIR


class Database:
    """
    Класс базs данных, по сути просто нужен для объединения базы данных и методов для взаимодействия с ней
    """
    USERS_DATABASE: dict[str, dict[str, any]] = {}

    @staticmethod
    def add_data(**kwargs):
        new_id = str(int(list(Database.USERS_DATABASE.keys())[-1]) + 1) if len(Database.USERS_DATABASE.keys()) != 0 else '0'
        Database.USERS_DATABASE[new_id] = {}
        for key, value in kwargs.items():
            Database.USERS_DATABASE[new_id][key] = value

    @staticmethod
    def fill_database_with_test_data() -> None:
        """
        Загрузить тестовые данные в бд из заранее заготовленного файла.
        Так как данные берутся с json тут всё в стрингах, в преобразовании смысла пока не вижу.

        Returns:
            None
        """
        with open(f'{APP_DIR}/internal/db/data/test_data.json', 'r') as file:
            Database.USERS_DATABASE = json.load(file)

    @staticmethod
    def save_data_base(filename: str):
        pass

    @staticmethod
    def load_data_base(filename: str):
        pass
