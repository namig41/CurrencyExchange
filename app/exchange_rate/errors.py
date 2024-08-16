from requestschema.http_response import HTTPResponse

from response.common_error import (DatabaseError,
                                   RequiredFieldMissingError, 
                                   BadRequest,
                                   NotFound,
                                   Conflict)

class ExchangeRateMissingError(BadRequest):
    def __init__(self):
        super().__init__('Currency pair codes are missing in the request')

class ExchangeRateNotFoundError(NotFound):
    def __init__(self, currency_pair):
        super().__init__(f'Exchange rate for pair "{currency_pair}" not found')
