from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import (
    Any,
    Generic,
    TypeVar,
)


ET = TypeVar("ET", bound=Any)


@dataclass
class BaseEntity(ABC, Generic[ET]):
    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self): ...
