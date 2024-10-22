from dataclasses import dataclass

from application.exceptions.http.base import HTTPResponseException

@dataclass(eq=False)
class BadRequestException(HTTPResponseException):
    
    code: int = 400
        
    @property
    def message(self):
        return 'Bad request'

@dataclass(eq=False)
class NotFoundException(HTTPResponseException):
    
    code: int = 404
    
    @property
    def message(self):
        return 'Not Found'

@dataclass(eq=False)
class ConflictException(HTTPResponseException):
    
    code: int = 409
    
    @property
    def message(self):
        return 'Conflict error'
    
@dataclass(eq=False)
class InternalServerException(HTTPResponseException):
        
    @property
    def message(self):
        return 'Internal Sever Error'

@dataclass(eq=False)
class RequiredFieldException(BadRequestException):
        
    @property
    def message(self):
        return 'Required field is missing'

@dataclass(eq=False)
class DatabaseException(InternalServerException):
        
    @property
    def message(self):
        return 'Database not exist'
