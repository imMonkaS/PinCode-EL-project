from fastapi import APIRouter

from routers.status import status_router

router = APIRouter()
router.include_router(status_router)
