from internal.repositories.db.models import BaseUser


class GetUserResponse(BaseUser):
    age: int
