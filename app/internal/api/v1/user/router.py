from fastapi import APIRouter
from internal.api.v1.user.profile import USER_PROFILE_ROUTER

USER_ROUTER = APIRouter(
    prefix='/user'
)

USER_ROUTER.include_router(USER_PROFILE_ROUTER)
