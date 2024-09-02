from dataclasses import dataclass


from domain.value_objects.currency import Currency
from domain.entities.money import Money

@dataclass(frozen=True)
class ExchangeRate:
    id: int
    from_currency: Currency
    to_currency: Currency
    rate: float
    
    def forward_convert(self, amount: Money) -> Money:
        """
        Конвертирует сумму в базовой валюте в котируемую валюту.

        :param amount: Сумма в базовой валюте.
        :return: Сумма в котируемой валюте.
        """
        if amount.currency != self.from_currency:
            raise ValueError(f"Amount currency must be {self.from_currency}")

        converted_amount = amount.amount * self.rate
        return Money(currency=self.to_currency, amount=converted_amount)

    def reverse_convert(self, amount: Money):

        """
        Конвертирует сумму в базовой валюте в котируемую валюту.
        :param amount: Сумма в базовой валюте.
        :return: Сумма в котируемой валюте.
        """
        if amount.currency != self.from_currency:
            raise ValueError(f"Amount currency must be {self.from_currency}")

        converted_amount = amount.amount / self.rate
        return Money(currency=self.to_currency, amount=converted_amount)

    def update_exchange_rate(self, new_rate: float):
        """
        Обновляет курс обмена для данной валютной пары.

        :param new_rate: Новый курс обмена.
        """
        self.rate = new_rate

    def _validate(self):
        if self.to_currency == self.from_currency:
            raise ValueError("CurrencyPair currencies must match ExchangeRate currencies.")

    def __repr__(self):
        return f"{self.from_currency}/{self.to_currency} @ {self.rate}"
