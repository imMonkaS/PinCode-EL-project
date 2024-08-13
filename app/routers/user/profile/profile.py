from fastapi import APIRouter

from routers.user.schemas.request.create import CreateProfileRequest
from internal.services.user import UserService
from routers.user.schemas.response.get import GetUserResponse

crud_router = APIRouter(
    tags=['user_profile']
)


# register
@crud_router.post('/')
def register_user_profile(
        request_data: CreateProfileRequest
):
    us = UserService()
    us.create(**request_data.model_dump())
    return 'User created'


# get
@crud_router.get('/{id}')
def get_user_profile(id: str) -> GetUserResponse:
    us = UserService()
    return us.get_by_id(id)


# update
@crud_router.patch('/{id}')
def patch_update_user_profile(id: str):
    pass


@crud_router.put('/{id}')
def put_update_register_user_profile(id: str):
    pass


# delete
@crud_router.post('/{id}')
def delete_user_profile(id: str):
    pass
