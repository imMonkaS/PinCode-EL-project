from fastapi import APIRouter

from internal.dependencies.user import UserServiceDependency
from internal.routers.user.schemas.request.create import CreateProfileRequest
from internal.services.user import UserService
from internal.routers.user.schemas.response.get import GetUserResponse

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
        'user_id': user_id
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
def patch_update_user_profile(
        id: int,
        service: UserServiceDependency
):
    pass


@user_profile_router.put('/{id}')
def put_update_register_user_profile(
        id: int,
        service: UserServiceDependency
):
    pass


# delete
@user_profile_router.post('/{id}')
def delete_user_profile(
        id: int,
        service: UserServiceDependency
):
    pass
