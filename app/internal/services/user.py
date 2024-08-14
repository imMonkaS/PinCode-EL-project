from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from internal.routers.user.schemas.response.get import GetUserResponse


class UserService:
    def __init__(self, user_repo):
        self.user_repository = user_repo

    def create(
            self,
            login: str,
            password: str,
            first_name: str,
            birth_date: date,
            last_name: str = None,
            middle_name: str = None,
            work_experience: int = 0,
    ) -> str:
        user_id = self.user_repository.create_one(
            login=login,
            password=password,
            first_name=first_name,
            birth_date=birth_date,
            last_name=last_name,
            middle_name=middle_name,
            work_experience=work_experience
        )
        return user_id

    def get_by_id(self, user_id: int) -> GetUserResponse:
        user_data = self.user_repository.get_one(user_id).copy()

        user_data.pop('password')
        user_data['age'] = relativedelta(datetime.today(), user_data['birth_date']).years
        return GetUserResponse.model_validate(user_data)

    # @staticmethod
    # def update_by_id(
    #         user_id: str,
    #         login: str = None,
    #         password: str = None,
    #         first_name: str = None,
    #         birth_date: date = None,
    #         last_name: str = None,
    #         middle_name: str = None,
    #         work_experience: int = None,
    # ):
    #     data = {
    #         'login': login,
    #         'password': password,
    #         'first_name': first_name,
    #         'birth_date': birth_date,
    #         'last_name': last_name,
    #         'middle_name': middle_name,
    #         'work_experience': work_experience
    #     }
    #
    #     data = {key: value for key, value in data.items() if value is not None}
    #     Database.change_data(user_id, **data)
    #
    # @staticmethod
    # def delete_by_id(user_id: str):
    #     Database.delete_user(user_id)
