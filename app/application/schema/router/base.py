from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Generic,
    TypeVar,
)

from application.schema.http.request import HTTPRequest
from domain.value_objects.base import BaseValue


ST = TypeVar("SC", bound=BaseValue)


@dataclass
class BaseSchema(ABC, Generic[ST]):

    @staticmethod
    @abstractmethod
    def check_request(self, request: HTTPRequest): ...

    @staticmethod
    @abstractmethod
    def parse_request(self, request: HTTPRequest) -> ST: ...
