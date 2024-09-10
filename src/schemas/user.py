from datetime import date, datetime

from dateutil.relativedelta import relativedelta
from pydantic import BaseModel, field_validator

from utils.password_utils import get_password_hash


class BaseUserSchema(BaseModel):
    login: str
    last_name: str
    first_name: str
    middle_name: str | None = None
    birth_date: date
    work_experience: int


class CreateUserSchema(BaseUserSchema, validate_assignment=True):
    password: str

    @field_validator('password')
    @classmethod
    def password_hash(cls, v):
        if v is not None:
            return get_password_hash(v)


class GetUserSchema(BaseUserSchema):
    user_id: int
    age: int = 0

    def calculate_age(self, birth_date):
        self.age = relativedelta(datetime.today(), birth_date).years


class UpdateUserSchema(CreateUserSchema):
    login: str | None = None
    password: str | None = None
    last_name: str | None = None
    first_name: str | None = None
    middle_name: str | None = None
    birth_date: date | None = None
    work_experience: int | None = None


class ReplaceUserSchema(CreateUserSchema):
    pass
