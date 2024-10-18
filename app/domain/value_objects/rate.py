from dataclasses import dataclass
from decimal import Decimal

from domain.exceptions.rate import RateIsNegativeException


@dataclass(frozen=True)
class Rate:
    value: Decimal
    
    @property
    def inverted(self) -> Decimal:
        return 1. / self.value
    
    def validate(self):
        if self.value < 0:
            raise RateIsNegativeException()