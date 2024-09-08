from internal.schemas import GetUserSchema
from pydantic import BaseModel


class DefaultUserResponse(BaseModel):
    status: int
    message: str
    data: list | dict | None = None


class GetUserResponse(DefaultUserResponse):
    data: GetUserSchema


class GetAllUsersResponse(DefaultUserResponse):
    data: list[GetUserSchema]
