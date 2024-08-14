from datetime import date

from internal.repositories.db.models.baseuser import BaseUser


class UpdateUserRequest(BaseUser, validate_assignment=True):
    login: str | None = None
    password: str | None = None
    last_name: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    birth_date: date | None = None
    work_experience: int | None = None
