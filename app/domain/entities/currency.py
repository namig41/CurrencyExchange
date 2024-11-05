from dataclasses import (
    dataclass,
    field,
)
from itertools import count

from domain.entities.base import BaseEntity
from domain.value_objects.currency_code import Code


@dataclass
class Currency(BaseEntity):
    id: int = field(  # noqa: A003
        default_factory=count().__next__,
        kw_only=True,
    )
    code: Code
    fullname: str
    sign: str

    def validate(self): ...

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: "Currency") -> bool:
        return self.code == other.code
