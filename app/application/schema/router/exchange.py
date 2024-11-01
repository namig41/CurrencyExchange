from dataclasses import dataclass
from decimal import Decimal

from application.exceptions.http.exchange import ExchangeNotFoundException
from application.exceptions.http.exchange_rate import ExchangeRateMissingException
from application.schema.http.request import HTTPRequest
from application.router import exchange_rate
from application.schema.router.base import BaseSchema
from application.schema.router.exchange_rate import ExchageRateDetailSchema
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from domain.services.currency_exchange_service import exchange, reverse_exchange, cross_exchange
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_exchange_entity_to_document, convert_exchange_rate_entity_to_document, convert_exchanges_entity_to_document

@dataclass
class ExchageConvertSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            return ExchangeNotFoundException()
        
        required_fields = ["from", "to", "amount"]
        missing_fields = [field for field in required_fields if field not in request.param]

        if missing_fields:
            raise ExchangeNotFoundException() 
        
    
    def parse_request(
        request: HTTPRequest,
        exchange_rates_repository: BaseExchangeRatesRepository
    ) -> ExchangeRate: 
        try:
            ExchageConvertSchema.check_request(request)
            
            base_code = request.param["from"][0]
            target_code = request.param["to"][0]
            amount = Decimal(request.param["amount"][0])
            
            conversion_result = exchange(base_code, target_code, amount, exchange_rates_repository)
            if conversion_result:
                exchange_rate, converted_amount = conversion_result
                return convert_exchange_entity_to_document(exchange_rate, amount, converted_amount)
            
            conversion_result = reverse_exchange(base_code, target_code, amount, exchange_rates_repository)
            if conversion_result:
                exchange_rate, converted_amount = conversion_result
                return convert_exchange_entity_to_document(exchange_rate, amount, converted_amount)
            
            conversion_result = cross_exchange(base_code, target_code, amount, exchange_rates_repository)
            if conversion_result:
                exchange_rates, converted_amount = conversion_result
                return convert_exchanges_entity_to_document(exchange_rates, amount, converted_amount)
            
            raise ExchangeNotFoundException()
        
        except ApplicationException as exception:
            raise exception
        