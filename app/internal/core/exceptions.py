class AppException(Exception):
    msg: str | None = NotImplemented
    error_code = 1
    status_code: int = NotImplemented

    def __init__(self, msg=''):
        super().__init__()
        self.msg = msg or self.msg

    def __str__(self):
        return self.msg or self.__doc__ or self.__class__.__name__

    def __call__(self):
        return str(self)


class UnknownException(AppException):
    msg = 'Service error'
    error_code = 1
    status_code = 500


class CustomValidationException(AppException):
    msg = 'Pydantic validation error'
    error_code = 2
    status_code = 422


class UserDoesNotExistException(AppException):
    msg = 'User does not exist'
    error_code = 3
    status_code = 404
