from datetime import date

from pydantic import BaseModel

from internal.repositories.db.models.baseuser import BaseUser


class CreateProfileRequest(BaseUser):
    password: str
