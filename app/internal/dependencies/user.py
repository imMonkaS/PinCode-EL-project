from typing import Annotated

from fastapi import Depends
from internal.dependencies.db import DBSessionDependency
from internal.repositories.db.user import UserRepository
from internal.services.user import UserService


def user_repository_dependency(session: DBSessionDependency):
    return UserRepository(session=session)


UserRepositoryDependency = Annotated[UserRepository, Depends(user_repository_dependency)]


def user_service_dependency(repo: UserRepositoryDependency):
    return UserService(user_repo=repo)


UserServiceDependency = Annotated[UserService, Depends(user_service_dependency)]
