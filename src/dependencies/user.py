from typing import Annotated

from fastapi import Depends

from repositories.user import UserRepository
from services.user import UserService

UserRepositoryDependency = Annotated[UserRepository, Depends(UserRepository)]


def user_service_dependency(repo: UserRepositoryDependency):
    return UserService(user_repo=repo)


UserServiceDependency = Annotated[UserService, Depends(user_service_dependency)]
