from dataclasses import dataclass

from application.exceptions.http.common import BadRequestException, ConflictException, NotFoundException

@dataclass(eq=False)
class CurrencyCodeMissingException(BadRequestException):
    
    @property
    def message(self):
        return 'Bad request'

@dataclass(eq=False)
class CurrencyNotFoundException(NotFoundException):        
    @property
    def message(self):
        return 'Currency not found'

@dataclass(eq=False)
class CurrencyAlreadyExistsException(ConflictException):
    
    @property
    def message(self):
        return 'Currency with code already exists'