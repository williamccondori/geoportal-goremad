class ApiException(Exception):
    status_code = 400

    def __init__(self, message: str = None):
        super().__init__(message)
