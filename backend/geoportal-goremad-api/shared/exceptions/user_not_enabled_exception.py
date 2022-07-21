from shared.exceptions.shared.api_exception import ApiException


class UserNotEnabledException(ApiException):
    def __init__(self):
        super().__init__("geo.goremad.user_not_enabled")
        self.status_code = 403
