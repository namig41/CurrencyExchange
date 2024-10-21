from dataclasses import dataclass
from typing import Iterable
from application.exceptions.http.exchange_rate import ExchangeRateMissingException
from application.http.request.http_request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document, convert_exchange_rate_entity_to_document

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
             
@dataclass
class ExchageRatesDetailSchema(BaseSchema):
    
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
            
            # TODO: реализовать сложный запрос с помощью join
            # exchange_rate: ExchangeRate = exchange_rates_repository.
            
            return convert_exchange_rate_entity_to_document(exchange_rate)
        except ApplicationException as exception:
            raise exception
        
        
        # from_currency = self.dao_currencies.find_by(code=request.body["baseCurrencyCode"][0])
        # to_currency = self.dao_currencies.find_by(code=request.body["targetCurrencyCode"][0])

        # if not from_currency:
        #     return CurrencyNotFoundError(request.body["baseCurrencyCode"][0])
        
        # if not to_currency:
        #     return CurrencyNotFoundError(request.body["targetCurrencyCode"][0])
        
        # exchange_rate_data = {
        #     "BaseCurrencyId": from_currency["id"],
        #     "TargetCurrencyId": to_currency["id"],
        #     "Rate": float(request.body["rate"][0])
        # }

        # self.dao_exchange_rate.insert(exchange_rate_data)

        # exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
        #                                       TargetCurrencyId=to_currency["id"])
        
        # exchange  = {
        #     "id": exchange_rate["id"],
        #     "baseCurrency": from_currency,
        #     "targetCurrency": to_currency,
        #     "rate": exchange_rate["rate"],
        # }

        # return SuccessResponse(exchange)