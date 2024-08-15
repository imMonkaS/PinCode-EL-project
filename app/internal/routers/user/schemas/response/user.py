from internal.models import BaseUser
from pydantic import BaseModel


class GetUserResponse(BaseUser):
    age: int


class DefaultUserResponse(BaseModel):
    status: int
    message: str
    data: dict | list | None = None
