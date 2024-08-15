from fastapi import APIRouter
from internal.dependencies.user import UserServiceDependency
from internal.routers.user.schemas.request import (CreateProfileRequest,
                                                   UpdateUserRequest)
from internal.routers.user.schemas.response import GetUserResponse
from internal.routers.user.schemas.response.user import DefaultUserResponse

USER_PROFILE_ROUTER = APIRouter(
    prefix='/profile',
    tags=['user_profile']
)


# register
@USER_PROFILE_ROUTER.post('/')
def register_user_profile(
        request_data: CreateProfileRequest,
        service: UserServiceDependency
) -> DefaultUserResponse:
    user_id = service.create(**request_data.model_dump())
    return DefaultUserResponse(
        status=200,
        message='Success',
        data={
            'user_id': user_id,
            'action': 'Created'
        }
    )


# get
@USER_PROFILE_ROUTER.get('/{id}')
def get_user_profile(
        id: int,
        service: UserServiceDependency
) -> GetUserResponse:
    return service.get_by_id(id)


# update
@USER_PROFILE_ROUTER.patch('/{id}')
def update_user_profile(
        id: int,
        request_data: UpdateUserRequest,
        service: UserServiceDependency
) -> DefaultUserResponse:
    updates = service.update_by_id(id, **request_data.model_dump())
    return DefaultUserResponse(
        status=200,
        message='Success',
        data={
            'user_id': id,
            'action': 'Updated',
            'updates_amount': updates
        }
    )


@USER_PROFILE_ROUTER.put('/{id}')
def replace_user_profile(
        id: int,
        request_data: UpdateUserRequest,
        service: UserServiceDependency
) -> DefaultUserResponse:
    user_id = service.replace_by_id(id, **request_data.model_dump())
    return DefaultUserResponse(
        status=200,
        message='Success',
        data={
            'user_id': user_id,
            'action': 'Replaced',
        }
    )


# delete
@USER_PROFILE_ROUTER.delete('/{id}')
def delete_user_profile(
        id: int,
        service: UserServiceDependency
) -> DefaultUserResponse:
    user_id = service.delete_by_id(id)
    return DefaultUserResponse(
        status=200,
        message='Success',
        data={
            'user_id': user_id,
            'action': 'Deleted'
        }
    )
