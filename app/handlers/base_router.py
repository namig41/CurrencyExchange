from abc import ABC, abstractmethod

from handlers.http_request import HTTPRequest
from handlers.http_response import HTTTPResponse

class BaseRouter(ABC):
    
    @abstractmethod
    def handle_get(self, request: HTTPRequest) -> HTTTPResponse:
        pass

    @abstractmethod
    def handle_post(self, request: HTTPRequest) -> HTTTPResponse:
        pass


