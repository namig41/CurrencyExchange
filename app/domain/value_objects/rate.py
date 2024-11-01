from dataclasses import dataclass
from decimal import Decimal, getcontext

from domain.exceptions.rate import RateIsNegativeException
from domain.value_objects.base import BaseValue

getcontext().prec = 10

# TODO: Необходимо вызвать конструктор с типом Rate(Decimal) 

@dataclass(frozen=True)
class Rate(BaseValue[float]):
    value: Decimal
    
    @property
    def inverted(self) -> Decimal:
        return Decimal(1) / Decimal(self.value)
    
    def validate(self):
        if self.value < 0:
            raise RateIsNegativeException()
        
    def as_generic_type(self) -> float:
        return float(self.value)