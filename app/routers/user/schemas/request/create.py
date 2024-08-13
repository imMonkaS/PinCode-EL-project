from datetime import date

from pydantic import BaseModel


class CreateProfileRequest(BaseModel):
    login: str
    password: str
    last_name: str
    first_name: str
    middle_name: str
    birth_date: date
    work_experience: int
