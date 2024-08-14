from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from internal.core.exception_handlers import (unknown_exception_handler,
                                              validation_exception_handler)
from internal.routers.router import router


def add_exceptions(app: FastAPI):
    app.add_exception_handler(Exception, unknown_exception_handler)
    app.add_exception_handler(RequestValidationError, validation_exception_handler)


def include_routers(app: FastAPI):
    app.include_router(router)


def create_app() -> FastAPI:
    app = FastAPI(
        root_path='/api'
    )

    add_exceptions(app)
    include_routers(app)

    return app
