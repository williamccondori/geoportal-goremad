from shared.exceptions.shared.api_exception import ApiException


class NotZipException(ApiException):
    def __init__(self):
        super().__init__("geo.goremad.zip.not_zip")
        self.status_code = 400


class ZipTooBigException(ApiException):
    def __init__(self):
        super().__init__("geo.goremad.zip.too_big")
        self.status_code = 400
