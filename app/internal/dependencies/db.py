from typing import Annotated

from fastapi.params import Depends
from internal.repositories.db.helpers import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

DBSessionDependency = Annotated[AsyncSession, Depends(get_async_session)]
