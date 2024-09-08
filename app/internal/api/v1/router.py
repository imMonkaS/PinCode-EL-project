from fastapi import APIRouter
from internal.api.v1.user.router import USER_ROUTER

V1_ROUTER = APIRouter(prefix='/v1')
V1_ROUTER.include_router(USER_ROUTER)
