from datetime import date

from pydantic import BaseModel


class GetUserResponse(BaseModel):
    login: str
    last_name: str
    first_name: str
    middle_name: str
    birth_date: date
    work_experience: int
    age: int
