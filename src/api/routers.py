from fastapi import APIRouter

from api.profile import USER_PROFILE_ROUTER
from api.status import STATUS_ROUTER

ROUTER = APIRouter()
ROUTER.include_router(STATUS_ROUTER)
ROUTER.include_router(USER_PROFILE_ROUTER)
