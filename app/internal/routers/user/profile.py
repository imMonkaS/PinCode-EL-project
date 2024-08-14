from fastapi import APIRouter
from internal.dependencies.user import UserServiceDependency
from internal.routers.user.schemas.request import (CreateProfileRequest,
                                                   UpdateUserRequest)
from internal.routers.user.schemas.response import GetUserResponse

user_profile_router = APIRouter(
    prefix='/profile',
    tags=['user_profile']
)


# register
@user_profile_router.post('/')
def register_user_profile(
        request_data: CreateProfileRequest,
        service: UserServiceDependency
):
    user_id = service.create(**request_data.model_dump())
    return {
        'user_id': user_id,
        'action': 'Created'
    }


# get
@user_profile_router.get('/{id}')
def get_user_profile(
        id: int,
        service: UserServiceDependency
) -> GetUserResponse:
    return service.get_by_id(id)


# update
@user_profile_router.patch('/{id}')
def update_user_profile(
        id: int,
        request_data: UpdateUserRequest,
        service: UserServiceDependency
):
    updates = service.update_by_id(id, **request_data.model_dump())
    return {
        'user_id': id,
        'action': 'Updated',
        'Updates_amount': updates
    }


@user_profile_router.put('/{id}')
def replace_user_profile(
        id: int,
        request_data: UpdateUserRequest,
        service: UserServiceDependency
):
    user_id = service.replace_by_id(id, **request_data.model_dump())
    return {
        'user_id': user_id,
        'action': 'Replaced',
    }


# delete
@user_profile_router.post('/{id}')
def delete_user_profile(
        id: int,
        service: UserServiceDependency
):
    user_id = service.delete_by_id(id)
    return {
        'user_id': user_id,
        'action': 'Deleted'
    }
