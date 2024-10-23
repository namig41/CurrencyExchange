from dataclasses import dataclass
from decimal import Decimal

from domain.exceptions.rate import RateIsNegativeException


@dataclass(frozen=True)
class Code:
    value: str
    
    def validate(self):
        if len(self.value) != 3:
            raise RateIsNegativeException()