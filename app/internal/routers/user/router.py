from fastapi import APIRouter

from internal.routers.user.profile import user_profile_router

user_router = APIRouter(
    prefix='/user'
)

user_router.include_router(user_profile_router)
