from dataclasses import dataclass, field
from uuid import uuid4

from domain.value_objects.base import BaseValue

@dataclass(frozen=True)
class Currency(BaseValue):
    id: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
    code: str
    fullname: str
    sign: str
