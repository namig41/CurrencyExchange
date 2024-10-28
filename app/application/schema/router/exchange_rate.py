from dataclasses import dataclass
from decimal import Decimal
from application.exceptions.http.exchange_rate import ExchangeRateMissingException, ExchangeRateNotFoundException
from application.http.request.http_request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from domain.value_objects.rate import Rate
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document, convert_exchange_rate_entity_to_document, convert_exchange_rates_entity_to_document

@dataclass
class ExchageRateDetailSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 2:
            raise ExchangeRateMissingException()
    
    def parse_request(
        request: HTTPRequest,
        exchange_rates_repository: BaseExchangeRatesRepository
    ) -> ExchangeRate:
        
        try:
            ExchageRateDetailSchema.check_request(request)
            
            currency_pair = request.parts[1]
            base_code, target_code = currency_pair[:3], currency_pair[3:]
                        
            exchange_rate: ExchangeRate = exchange_rates_repository.get_exchange_rate_by_codes(base_code, target_code)
                        
            if exchange_rate is None:
                raise ExchangeRateNotFoundException()
                        
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
            rate: Rate = Rate(Decimal(request.body["rate"][0]))
            
            exchange_rate: ExchangeRate = ExchangeRate(base_currency, target_currency, rate)  
            
            exchange_rates_repository.update_exchange_rate(exchange_rate)
                                    
            return convert_exchange_rate_entity_to_document(exchange_rate)
        except ApplicationException as exception:
            raise exception
             
