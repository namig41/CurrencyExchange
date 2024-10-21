from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from http.client import HTTPResponse

from application.http.request.http_request import HTTPRequest

@dataclass
class BaseRouter(ABC):
    
    prefix: str = field(default="/")
    
    @abstractmethod
    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        ...

    @abstractmethod
    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        ...

    @abstractmethod
    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        ...
