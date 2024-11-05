from decimal import Decimal
from typing import (
    Iterable,
    Optional,
)

from domain.entities.exchange_rate import ExchangeRate
from domain.interface.repository import ICurrencyExchangeRateRepository


def get_exchange_rate(
    base_code: str,
    target_code: str,
    currency_exchange_rate_repository: ICurrencyExchangeRateRepository,
) -> Optional[ExchangeRate]:
    """Получить курс обмена между двумя валютами."""
    exchange_rate: ExchangeRate = (
        currency_exchange_rate_repository.get_exchange_rate_by_codes(
            base_code,
            target_code,
        )
    )
    if exchange_rate is None:
        return None
    return exchange_rate


def exchange(
    base_code: str,
    target_code: str,
    amount: Decimal,
    currency_exchange_rate_repository: ICurrencyExchangeRateRepository,
) -> Optional[tuple[Iterable[ExchangeRate], Decimal]]:
    """Выполнить прямой обмен валюты."""
    exchange_rate = get_exchange_rate(
        base_code,
        target_code,
        currency_exchange_rate_repository,
    )
    if exchange_rate is None:
        return None
    return exchange_rate, exchange_rate.rate.value * amount


def reverse_exchange(
    base_code: str,
    target_code: str,
    amount: Decimal,
    currency_exchange_rate_rate_repository: ICurrencyExchangeRateRepository,
) -> Optional[tuple[Iterable[ExchangeRate], Decimal]]:
    """Выполнить обратный обмен валюты."""
    exchange_rate = get_exchange_rate(
        target_code,
        base_code,
        currency_exchange_rate_rate_repository,
    )
    if exchange_rate is None:
        return None
    return exchange_rate, exchange_rate.rate.inverted * amount


def cross_exchange(
    base_code: str,
    target_code: str,
    amount: Decimal,
    currency_exchange_rate_repository: ICurrencyExchangeRateRepository,
    base_currency: str = "USD",
) -> Optional[tuple[Iterable[ExchangeRate], Decimal]]:
    """Выполнить кросс-обмен через базовую валюту USD."""

    exchange_rate_1 = get_exchange_rate(
        base_code,
        base_currency,
        currency_exchange_rate_repository,
    )
    exchange_rate_2 = get_exchange_rate(
        base_currency,
        target_code,
        currency_exchange_rate_repository,
    )

    if exchange_rate_1 is None or exchange_rate_2 is None:
        return None

    return [
        exchange_rate_1,
        exchange_rate_2,
    ], exchange_rate_1.rate.value * amount * exchange_rate_2.rate.value
