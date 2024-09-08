from fastapi import APIRouter
from internal.api.status import STATUS_ROUTER
from internal.api.v1.router import V1_ROUTER

ROUTER = APIRouter()
ROUTER.include_router(STATUS_ROUTER)
ROUTER.include_router(V1_ROUTER)
