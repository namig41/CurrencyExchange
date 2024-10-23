from dataclasses import dataclass
from decimal import Decimal
from typing import Iterable

from application.exceptions.http.exchange_rate import ExchangeRateMissingException
from application.http.request.http_request import HTTPRequest
from application.schema.router.base import BaseSchema
from application.schema.router.exchange_rate import ExchageRateDetailSchema
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from domain.value_objects.rate import Rate
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_exchange_rate_entity_to_document, convert_exchange_rates_entity_to_document


@dataclass
class ExchageRatesDetailSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            return ExchangeRateMissingException()
    
    def parse_request(
        request: HTTPRequest,
        exchange_rates_repository: BaseExchangeRatesRepository
    ) -> Iterable[ExchangeRate]:
        
        try:
            ExchageRatesDetailSchema.check_request(request)
            exchange_rates: list[ExchangeRate] = exchange_rates_repository.get_exchange_rates()
            return convert_exchange_rates_entity_to_document(exchange_rates)
        except ApplicationException as exception:
            raise exception        
        
@dataclass
class ExchageRatesCreateSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            return ExchangeRateMissingException()
    
    def parse_request(
        request: HTTPRequest,
        currencies_repository: BaseCurrenciesRepository,
        exchange_rates_repository: BaseExchangeRatesRepository
    ) -> Iterable[ExchangeRate]:
        
        try:
            ExchageRateDetailSchema.check_request(request)
            
            base_currency_code = request.body["baseCurrencyCode"][0]
            target_currency_code = request.body["targetCurrencyCode"][0]
            
            base_currency = currencies_repository.get_currency_by_code(code=base_currency_code)
            target_currency = currencies_repository.get_currency_by_code(code=target_currency_code)
            rate = Rate(Decimal(request.body["rate"][0]))

            exchange_rate = ExchangeRate(base_currency, target_currency, rate)
    
            exchange_rates_repository.add_exchange_rate(exchange_rate)
            
            return convert_exchange_rate_entity_to_document(exchange_rate)
        except ApplicationException as exception:
            raise exception