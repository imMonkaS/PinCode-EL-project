from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse, Response
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from utils.exceptions import (CustomValidationException, IntegrityException,
                              ProgrammingException, UnknownException,
                              UserDoesNotExistException)


def unknown_exception_handler(request, exc) -> Response:
    exc = UnknownException()
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def validation_exception_handler(request, exc) -> Response:
    validation_exception = CustomValidationException()
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            'message': validation_exception.msg,
            'error_code': jsonable_encoder(exc.errors())
        },
    )


def user_does_not_exist_exception_handler(request, exc) -> Response:
    exc = UserDoesNotExistException()
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def integrity_exception_handler(request, exc) -> Response:
    exc = IntegrityException()
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )


def programming_exception_handler(request, exc) -> Response:
    exc = ProgrammingException()
    return JSONResponse(
        status_code=exc.status_code,
        content={
            'message': exc.msg,
            'error_code': exc.error_code
        },
    )
