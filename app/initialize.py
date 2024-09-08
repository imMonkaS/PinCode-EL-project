from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from internal.api.router import ROUTER
from internal.core.exception_handlers import (
    unknown_exception_handler, user_does_not_exist_exception_handler,
    validation_exception_handler)
from internal.core.exceptions import UserDoesNotExistException


def add_exceptions(app: FastAPI):
    app.add_exception_handler(Exception, unknown_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(UserDoesNotExistException, user_does_not_exist_exception_handler)


def include_routers(app: FastAPI):
    app.include_router(ROUTER)


def create_app() -> FastAPI:
    app = FastAPI(
        root_path='/api'
    )

    add_exceptions(app)
    include_routers(app)

    return app
