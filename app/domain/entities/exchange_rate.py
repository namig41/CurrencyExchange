from dataclasses import dataclass, field
import decimal
from itertools import count

from domain.entities.base import BaseEntity
from domain.entities.currency import Currency
from domain.exceptions.exchange_rate import EqualCurrencyException
from domain.value_objects.base import BaseValue
from domain.value_objects.rate import Rate

@dataclass
class ExchangeRate(BaseEntity):
    id: int = field(
        default_factory=count().__next__,
        kw_only=True,
    )
    baseCurrency: Currency
    targetCurrency: Currency
    rate: Rate
    
    def validate(self):
        if self.baseCurrency == self.targetCurrency:
            raise EqualCurrencyException()
        
