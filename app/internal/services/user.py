from datetime import date, datetime
from dateutil.relativedelta import relativedelta

from internal.db.db import Database
from routers.user.schemas.response.get import GetUserResponse


class UserService:
    @staticmethod
    def create(
            login: str,
            password: str,
            first_name: str,
            birth_date: date,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = 0,
    ) -> str:
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
        user_id = Database.create_data(**data)
        return user_id

    @staticmethod
    def get_by_id(user_id: str) -> GetUserResponse:
        try:
            user_data = Database.get_user(user_id).copy()

            user_data.pop('password')
            user_data['age'] = relativedelta(datetime.today(), user_data['birth_date']).years

            return GetUserResponse.model_validate(user_data)
        except Exception as e:
            raise e

    @staticmethod
    def update_by_id(
            user_id: str,
            login: str = None,
            password: str = None,
            first_name: str = None,
            birth_date: date = None,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = None,
    ):
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
        Database.change_data(user_id, **data)

    @staticmethod
    def delete_by_id(user_id: str):
        Database.delete_user(user_id)
