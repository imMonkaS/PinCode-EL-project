import datetime

from internal.repositories.db.helpers import Base
from internal.schemas import GetUserSchema
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = 'users'
    __mapper_args__ = {'eager_defaults': True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(length=40), unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    first_name: Mapped[str] = mapped_column(String(length=20), nullable=False)
    middle_name: Mapped[str] = mapped_column(String(length=20), nullable=True)
    birth_date: Mapped[datetime.date]
    work_experience: Mapped[int] = mapped_column(default=0)

    def to_read_model(self) -> GetUserSchema:
        return GetUserSchema(
            user_id=self.id,
            login=self.login,
            last_name=self.last_name,
            first_name=self.first_name,
            middle_name=self.middle_name,
            birth_date=self.birth_date,
            work_experience=self.work_experience
        )
