from abc import ABC, abstractmethod

from handlers.http_request import HTTPRequest
from handlers.http_response import HTTPResponse

class BaseRouter(ABC):
    
    @abstractmethod
    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        pass

    @abstractmethod
    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

