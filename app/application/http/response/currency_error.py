from infrastructure.http.response.http_response import HTTPResponse

from infrastructure.http.response.common_error import (DatabaseError,
                                                           RequiredFieldMissingError,
                                                           BadRequest,
                                                           NotFound,
                                                           Conflict)

class CurrencyCodeMissingError(BadRequest):
    def __init__(self):
        super().__init__('Currency code is missing in the request')

class CurrencyNotFoundError(NotFound):
    def __init__(self):
        super().__init__(f'Currency not found')

class CurrencyAlreadyExistsError(Conflict):
    def __init__(self):
        super().__init__('Currency with code already exists')