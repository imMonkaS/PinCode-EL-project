from internal.repositories.db.models import BaseUser


class CreateProfileRequest(BaseUser):
    password: str
