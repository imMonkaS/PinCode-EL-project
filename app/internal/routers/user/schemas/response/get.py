from internal.repositories.db.models.baseuser import BaseUser


class GetUserResponse(BaseUser):
    age: int
