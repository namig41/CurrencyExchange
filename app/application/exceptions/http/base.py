from dataclasses import dataclass
from domain.exceptions.base import ApplicationException

@dataclass(eq=False)
class HTTPResponseException(ApplicationException):
    
    code: int
    
    @property
    def message(self):
        return 'Ошибка обработки запроса'
    

