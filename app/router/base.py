from abc import ABC, abstractmethod

from request.http_request import HTTPRequest
from response.http_response import HTTPResponse

class BaseRouter(ABC):
    
    @abstractmethod
    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        pass

    @abstractmethod
    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    @abstractmethod
    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass
