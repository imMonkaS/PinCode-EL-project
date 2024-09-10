from models import User
from repositories.base import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    """
    Репозирорий для работы с базой данных пользователя
    """
    model = User
