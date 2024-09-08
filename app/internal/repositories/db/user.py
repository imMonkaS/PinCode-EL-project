from internal.repositories.db.base import SQLAlchemyRepository
from internal.repositories.db.models import User


class UserRepository(SQLAlchemyRepository):
    """
    Репозирорий для работы с базой данных пользователя
    """
    model = User
