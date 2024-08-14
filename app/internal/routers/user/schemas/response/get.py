from datetime import date
from pydantic import Field

from internal.repositories.db.models.baseuser import BaseUser


class GetUserResponse(BaseUser):
    age: int
