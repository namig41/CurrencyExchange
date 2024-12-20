from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable

from infrastructure.repositories.base import (
    BaseCurrenciesRepository,
    BaseExchangeRatesRepository,
)
from infrastructure.repositories.converters import (
    convert_exchange_rate_entity_to_document,
    convert_exchange_rates_entity_to_document,
)

from application.exceptions.http.common import RequiredFieldMissingException
from application.exceptions.http.currency import CurrencyNotFoundException
from application.exceptions.http.exchange_rate import (
    ExchangeRateExisistException,
    ExchangeRateMissingException,
)
from application.schema.http.request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from domain.value_objects.rate import Rate


@dataclass
class ExchageRatesDetailSchema(BaseSchema):

    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            raise ExchangeRateMissingException()

    def parse_request(
        request: HTTPRequest,
        exchange_rates_repository: BaseExchangeRatesRepository,
    ) -> Iterable[ExchangeRate]:

        try:
            ExchageRatesDetailSchema.check_request(request)
            exchange_rates: list[ExchangeRate] = (
                exchange_rates_repository.get_exchange_rates()
            )
            return convert_exchange_rates_entity_to_document(exchange_rates)
        except ApplicationException as exception:
            raise exception


@dataclass
class ExchageRatesCreateSchema(BaseSchema):

    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            return ExchangeRateMissingException()

        required_fields = ["baseCurrencyCode", "targetCurrencyCode", "rate"]
        missing_fields = [
            field for field in required_fields if field not in request.body
        ]

        if missing_fields:
            raise RequiredFieldMissingException()

    def parse_request(
        request: HTTPRequest,
        currencies_repository: BaseCurrenciesRepository,
        exchange_rates_repository: BaseExchangeRatesRepository,
    ) -> Iterable[ExchangeRate]:

        try:
            ExchageRatesCreateSchema.check_request(request)

            base_currency_code = request.body["baseCurrencyCode"][0]
            target_currency_code = request.body["targetCurrencyCode"][0]
            rate = Rate(Decimal(request.body["rate"][0]))

            base_currency = currencies_repository.get_currency_by_code(
                currency_code=base_currency_code,
            )

            if base_currency is None:
                raise CurrencyNotFoundException()

            target_currency = currencies_repository.get_currency_by_code(
                currency_code=target_currency_code,
            )

            if target_currency is None:
                raise CurrencyNotFoundException()

            exchange_rate = ExchangeRate(base_currency, target_currency, rate)

            if exchange_rates_repository.get_exchange_rate_by_codes(
                base_currency.code,
                target_currency.code,
            ):
                raise ExchangeRateExisistException()

            exchange_rates_repository.add_exchange_rate(exchange_rate)

            return convert_exchange_rate_entity_to_document(exchange_rate)
        except ApplicationException as exception:
            raise exception
