class AppException(Exception):
    msg: str | None = NotImplemented
    error_code = 1
    status_code: int = NotImplemented
    system_prefix: str | None = NotImplemented

    def __init__(self, msg=''):
        super().__init__()
        self.msg = msg or self.msg

    def __str__(self):
        return self.msg or self.__doc__ or self.__class__.__name__

    def __call__(self):
        return str(self)


class UnknownException(AppException):
    system_prefix = 'APP'
    msg = 'Service error'
    error_code = 1
    status_code = 500


class CustomValidationException(AppException):
    system_prefix = 'PYDANTIC'
    msg = 'Pydantic validation error'
    error_code = 2
    status_code = 422


class SQLAlchemyModelsException(AppException):
    system_prefix = 'MODELS'


class UserDoesNotExistException(SQLAlchemyModelsException):
    msg = 'User does not exist'
    error_code = 3
    status_code = 404


class IntegrityException(SQLAlchemyModelsException):
    msg = 'Object with this name already exists'
    error_code = 4
    status_code = 409


class ProgrammingException(SQLAlchemyModelsException):
    msg = 'Something wrong with request'
    error_code = 5
    status_code = 400
