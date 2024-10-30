from dataclasses import dataclass
from decimal import Decimal

from domain.exceptions.rate import RateIsNegativeException
from domain.value_objects.base import BaseValue


@dataclass(frozen=True)
class Rate(BaseValue[float]):
    value: Decimal
    
    @property
    def inverted(self) -> Decimal:
        return 1. / self.value
    
    def validate(self):
        if self.value < 0:
            raise RateIsNegativeException()
        
    def as_generic_type(self) -> float:
        return float(self.value)