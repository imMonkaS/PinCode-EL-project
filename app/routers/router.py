from fastapi import APIRouter

from routers.status import status_router
from routers.user.router import user_router

router = APIRouter()
router.include_router(status_router)
router.include_router(user_router)
