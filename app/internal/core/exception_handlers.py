from fastapi.encoders import jsonable_encoder
from internal.core.exceptions import (CustomValidationException,
                                      UnknownException)
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY


def unknown_exception_handler(request, exc):
    exc = UnknownException()
    return JSONResponse(
        content={
            'message': exc.msg,
            'error_code': exc.error_code,
        },
        status_code=exc.status_code
    )


def validation_exception_handler(request, exc):
    validation_exception = CustomValidationException()
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            'error': validation_exception.msg,
            'detail': jsonable_encoder(exc.errors())
        },
    )
