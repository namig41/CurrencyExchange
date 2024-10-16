from dataclasses import dataclass
from decimal import Decimal

from domain.exceptions.rate import RateIsNegativeException


@dataclass(frozen=True)
class Rate:
    rate: Decimal
    
    @property
    def inverted(self) -> Decimal:
        return 1. / self.rate
    
    def validate(self):
        if self.rate < 0:
            raise RateIsNegativeException()