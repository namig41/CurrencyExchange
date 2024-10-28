from dataclasses import dataclass
from application.exceptions.http.common import BadRequestException, NotFoundException, RequiredFieldException

@dataclass(eq=False)
class ExchangeNotFoundException(NotFoundException):

    @property
    def message(self):
        return 'Exchange rate not found'
    
@dataclass(eq=False)
class ExchangeRateMissingException(RequiredFieldException):
    @property
    def message(self):
        return 'Exchange rate missing field'

@dataclass(eq=False)
class ExchangeRateNotFoundException(NotFoundException):
    
    @property
    def message(self):
        return f'Exchange rate for pair not found'
    
@dataclass(eq=False)
class ExchangeRateExisistException(NotFoundException):
    
    @property
    def message(self):
        return f'Exchange rate for pair exists'
   