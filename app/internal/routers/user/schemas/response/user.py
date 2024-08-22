from internal.models.user import GetUserModel
from pydantic import BaseModel


class DefaultUserResponse(BaseModel):
    status: int
    message: str
    data: dict | list | None = None


class GetUserResponse(DefaultUserResponse):
    data: GetUserModel
