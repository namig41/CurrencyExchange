from app.domain.entities.exchange_rate import ExchangeRate
from app.domain.value_objects.money import Money


class CurrencyPair:
    def __init__(self, base_currency: str, target_currency: str, exchange_rate: ExchangeRate):
        """
        :param base_currency: Базовая валюта (например, 'USD')
        :param target_currency: Котируемая валюта (например, 'EUR')
        :param exchange_rate: Объект ExchangeRate, содержащий курс обмена между валютами
        """
        if base_currency != exchange_rate.from_currency or target_currency != exchange_rate.to_currency:
            raise ValueError("CurrencyPair currencies must match ExchangeRate currencies.")

        self.base_currency = base_currency
        self.target_currency = target_currency
        self.exchange_rate = exchange_rate

    def convert_to_quote(self, amount: Money) -> Money:
        """
        Конвертирует сумму в базовой валюте в котируемую валюту.

        :param amount: Сумма в базовой валюте.
        :return: Сумма в котируемой валюте.
        """
        if amount.currency != self.base_currency:
            raise ValueError(f"Amount currency must be {self.base_currency}")

        converted_amount = amount.amount * self.exchange_rate.rate
        return Money(currency=self.target_currency, amount=converted_amount)

    def convert_to_base(self, amount: Money) -> Money:
        """
        Конвертирует сумму в котируемой валюте в базовую валюту.

        :param amount: Сумма в котируемой валюте.
        :return: Сумма в базовой валюте.
        """
        if amount.currency != self.target_currency:
            raise ValueError(f"Amount currency must be {self.target_currency}")

        converted_amount = amount.amount / self.exchange_rate.rate
        return Money(currency=self.target_currency, amount=converted_amount)

    def update_exchange_rate(self, new_rate: float):
        """
        Обновляет курс обмена для данной валютной пары.

        :param new_rate: Новый курс обмена.
        """
        self.exchange_rate.rate = new_rate

    def __repr__(self):
        return f"{self.base_currency}/{self.target_currency} @ {self.exchange_rate.rate}"
