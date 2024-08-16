from response.http_response import HTTPResponse
from response.common_error import (DatabaseError,
                                   RequiredFieldMissingError, 
                                   BadRequest,
                                   NotFound,
                                   Conflict)

class ExchangeRatesNotFoundError(NotFound):
    def __init__(self):
        super().__init__(f'Exchange rate not found')
