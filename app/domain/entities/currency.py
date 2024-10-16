from dataclasses import dataclass, field
from itertools import count
from uuid import uuid4

from domain.entities.base import BaseEntity

@dataclass
class Currency(BaseEntity):
    id: int = field(
        default_factory=count().__next__,
        kw_only=True,
    )
    code: str
    fullname: str
    sign: str
    
    def validate(self):
        ...
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other: 'Currency'):
        return self.code == other.code