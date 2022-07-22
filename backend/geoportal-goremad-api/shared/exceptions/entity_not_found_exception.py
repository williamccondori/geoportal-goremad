from shared.exceptions.shared.api_exception import ApiException


class EntityNotFoundException(ApiException):
    def __init__(self, entity_type: type):
        super().__init__("geo.goremad.entity_not_found.{}".format(entity_type))
