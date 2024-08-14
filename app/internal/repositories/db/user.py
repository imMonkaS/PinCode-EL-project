from datetime import date

from internal.repositories.db.db import UserDatabase


class UserRepository:
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

        user_id = self.db.create_user(**data)
        return user_id

    def get_one(self, user_id: int):
        return self.db.get_user(user_id)

    # def update(
    #         self,
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
    #
    # def delete(self, user_id: str):
    #     pass
