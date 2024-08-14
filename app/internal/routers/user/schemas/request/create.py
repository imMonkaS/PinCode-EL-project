from internal.repositories.db.models.baseuser import BaseUser


class CreateProfileRequest(BaseUser):
    password: str
