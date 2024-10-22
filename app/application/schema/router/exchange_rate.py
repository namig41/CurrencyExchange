from dataclasses import dataclass
from typing import Iterable
from application.exceptions.http.exchange_rate import ExchangeRateMissingException
from application.http.request.http_request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document, convert_exchange_rate_entity_to_document, convert_exchange_rates_entity_to_document

@dataclass
class ExchageRateDetailSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 2:
            raise ExchangeRateMissingException()
    
    def parse_request(
        request: HTTPRequest,
        currencies_repository: BaseCurrenciesRepository,
        exchange_rates_repository: BaseExchangeRatesRepository
    ) -> ExchangeRate:
        
        try:
            ExchageRateDetailSchema.check_request(request)
            
            currency_pair = request.parts[1]
            base_currency_code, target_currency_code = currency_pair[:3], currency_pair[3:]
            
            base_currency = currencies_repository.get_currency_by_code(code=base_currency_code)
            target_currency = currencies_repository.get_currency_by_code(code=target_currency_code)
            
            exchange_rate: ExchangeRate = exchange_rates_repository.get_exchange_rate_by_id(base_currency, target_currency)
            
            return convert_exchange_rate_entity_to_document(exchange_rate)
        except ApplicationException as exception:
            raise exception
        
        
@dataclass
class ExchageRateUpdateSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 2:
            raise ExchangeRateMissingException()
    
    def parse_request(
        request: HTTPRequest,
        currencies_repository: BaseCurrenciesRepository,
        exchange_rates_repository: BaseExchangeRatesRepository
    ) -> ExchangeRate:
        
        try:
            ExchageRateUpdateSchema.check_request(request)
            
            currency_pair = request.parts[1]
            base_currency_code, target_currency_code = currency_pair[:3], currency_pair[3:]
            
            base_currency = currencies_repository.get_currency_by_code(code=base_currency_code)
            target_currency = currencies_repository.get_currency_by_code(code=target_currency_code)
            
            # TODO: need to update exchange rate  
            exchange_rate: ExchangeRate = exchange_rates_repository.get_exchange_rate_by_id(base_currency, target_currency)
            
            return convert_exchange_rate_entity_to_document(exchange_rate)
        except ApplicationException as exception:
            raise exception
             
