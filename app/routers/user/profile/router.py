from fastapi import APIRouter

from routers.user.profile.profile import crud_router

user_profile_router = APIRouter(
    prefix='/profile'
)

user_profile_router.include_router(crud_router)
