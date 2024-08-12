from fastapi import APIRouter

crud_router = APIRouter(
    tags=['user_profile']
)


# register
@crud_router.post('/')
def register_user_profile():
    pass


# get
@crud_router.get('/{id}')
def get_user_profile(id: int):
    pass


# update
@crud_router.patch('/{id}')
def patch_update_user_profile(id: int):
    pass


@crud_router.put('/{id}')
def put_update_register_user_profile(id: int):
    pass


# delete
@crud_router.post('/{id}')
def delete_user_profile(id: int):
    pass
