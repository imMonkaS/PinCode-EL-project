from datetime import datetime

from internal.db.db import Database


class UserService:
    @staticmethod
    def create(
            login: str,
            password: str,
            first_name: str,
            birthdate: datetime.date,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = 0,
    ):
        data = {
            'login': login,
            'password': password,
            'first_name': first_name,
            'birthdate': birthdate,
            'last_name': last_name,
            'middle_name': middle_name,
            'work_experience': work_experience
        }

        data = {key: value for key, value in data.items() if value is not None}
        Database.add_data(**data)

    @staticmethod
    def get_one(

    ):
        pass

    @staticmethod
    def update(

    ):
        pass

    @staticmethod
    def delete(

    ):
        pass
