from typing import Annotated

from fastapi import APIRouter, Depends
from internal.api.v1.user.schemas.response import (DefaultUserResponse,
                                                   GetUserResponse)
from internal.api.v1.user.schemas.response.user import GetAllUsersResponse
from internal.dependencies.user import UserServiceDependency
from internal.schemas import (CreateUserSchema, ReplaceUserSchema,
                              UpdateUserSchema)

USER_PROFILE_ROUTER = APIRouter(
    prefix='/profile',
    tags=['user profile']
)


# register
@USER_PROFILE_ROUTER.post('/')
async def register_user_profile(
        request_data: Annotated[CreateUserSchema, Depends(CreateUserSchema)],
        service: UserServiceDependency
) -> GetUserResponse:
    user = await service.create(request_data)

    return GetUserResponse(
        status=200,
        message='Success',
        data=user
    )


@USER_PROFILE_ROUTER.get('/all')
async def get_all_users(
        service: UserServiceDependency
) -> GetAllUsersResponse:
    users = await service.get_all()

    return GetAllUsersResponse(
        status=200,
        message='Success',
        data=users
    )


# get
@USER_PROFILE_ROUTER.get('/{id}')
async def get_user_profile(
        id: int,
        service: UserServiceDependency
) -> GetUserResponse:
    user = await service.get_by_id(id)

    return GetUserResponse(
        status=200,
        message='Success',
        data=user
    )


# update
@USER_PROFILE_ROUTER.patch('/{id}')
async def update_user_profile(
        id: int,
        request_data: Annotated[UpdateUserSchema, Depends(UpdateUserSchema)],
        service: UserServiceDependency
) -> GetUserResponse:
    upd_user = await service.update_by_id(id, request_data)

    return GetUserResponse(
        status=200,
        message='Success',
        data=upd_user
    )


@USER_PROFILE_ROUTER.put('/{id}')
async def replace_user_profile(
        id: int,
        request_data: Annotated[ReplaceUserSchema, Depends(ReplaceUserSchema)],
        service: UserServiceDependency
) -> GetUserResponse:
    upd_user = await service.replace_by_id(id, request_data)
    return GetUserResponse(
        status=200,
        message='Success',
        data=upd_user
    )


# delete
@USER_PROFILE_ROUTER.delete('/{id}')
async def delete_user_profile(
        id: int,
        service: UserServiceDependency
) -> DefaultUserResponse:
    await service.delete_by_id(id)
    return DefaultUserResponse(
        status=200,
        message='Success',
        data={
            'user_id': id,
            'action': 'Deleted'
        }
    )
