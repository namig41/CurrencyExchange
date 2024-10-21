from dataclasses import dataclass
from application.exceptions.http.common import BadRequestException, NotFoundException, RequiredFieldException

@dataclass
class ExchangeNotFoundException(NotFoundException):

    @property
    def message(self):
        return 'Exchange rate not found'

class ExchangeRateMissingException(RequiredFieldException):
    @property
    def message(self):
        return 'Exchange rate missing field'

class ExchangeRateNotFoundException(NotFoundException):
    
    @property
    def message(self):
        return f'Exchange rate for pair not found'
   