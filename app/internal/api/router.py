from fastapi import APIRouter
from internal.api.status import STATUS_ROUTER
from internal.api.v1.user.router import USER_ROUTER

ROUTER = APIRouter()
ROUTER.include_router(STATUS_ROUTER)
ROUTER.include_router(USER_ROUTER)
