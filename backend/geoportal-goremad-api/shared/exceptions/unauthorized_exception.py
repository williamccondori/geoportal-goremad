from shared.exceptions.shared.api_exception import ApiException


class UnauthorizedException(ApiException):
    def __init__(self):
        super().__init__("geo.goremad.unauthorized")
        self.status_code = 401
        self.headers = {"WWW-Authenticate": "Bearer"},
