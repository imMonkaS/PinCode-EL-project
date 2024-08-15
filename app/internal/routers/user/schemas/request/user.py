from datetime import date

from internal.models import BaseUser


class CreateProfileRequest(BaseUser):
    password: str


class UpdateUserRequest(BaseUser, validate_assignment=True):
    login: str | None = None
    password: str | None = None
    last_name: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    birth_date: date | None = None
    work_experience: int | None = None
