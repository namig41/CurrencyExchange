from dataclasses import dataclass
from application.exceptions.http.common import BadRequestException, NotFoundException, RequiredFieldMissingException

@dataclass(eq=False)
class ExchangeRateMissingException(RequiredFieldMissingException):
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
   