from fastapi import APIRouter
from internal.routers.status import STATUS_ROUTER
from internal.routers.user.router import USER_ROUTER

ROUTER = APIRouter()
ROUTER.include_router(STATUS_ROUTER)
ROUTER.include_router(USER_ROUTER)
