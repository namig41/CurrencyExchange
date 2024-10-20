from dataclasses import dataclass
from application.exceptions.http.common import BadRequestException, NotFoundException, RequiredFieldException

@dataclass
class ExchangeNotFoundError(NotFoundException):

    @property
    def message(self):
        return 'Exchange rate not found'

class ExchangeRateMissingError(RequiredFieldException):
    @property
    def message(self):
        return 'Exchange rate missing field'

class ExchangeRateNotFoundError(NotFoundException):
    
    @property
    def message(self):
        return f'Exchange rate for pair not found'
   