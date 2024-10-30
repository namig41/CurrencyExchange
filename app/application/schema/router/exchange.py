from dataclasses import dataclass

from application.exceptions.http.exchange import ExchangeNotFoundException
from application.exceptions.http.exchange_rate import ExchangeRateMissingException
from application.schema.http.request import HTTPRequest
from application.router import exchange_rate
from application.schema.router.base import BaseSchema
from application.schema.router.exchange_rate import ExchageRateDetailSchema
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_exchange_entity_to_document, convert_exchange_rate_entity_to_document
    
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
            amount = float(request.param["amount"][0])
            
            exchange_rate = exchange_rates_repository.get_exchange_rate_by_codes(base_code, target_code)
            converted_amount = 0
            
            return convert_exchange_entity_to_document(exchange_rate, amount, converted_amount)
        except ApplicationException as exception:
            raise exception
        