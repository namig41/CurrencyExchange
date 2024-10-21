from dataclasses import dataclass
from typing import Iterable
from application.exceptions.http.common import RequiredFieldException
from application.exceptions.http.currency import CurrencyAlreadyExistsException, CurrencyNotFoundException
from application.exceptions.http.exchange_rate import ExchangeRateMissingException
from application.http.request.http_request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.currency import Currency
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document


@dataclass
class CurrenciesDetailSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            raise RequiredFieldException()
    
    def parse_request(request: HTTPRequest, currencies_repository: BaseCurrenciesRepository) -> Iterable[Currency]:
        
        try:
            CurrenciesDetailSchema.check_request(request)
            currencies: Iterable[Currency] = currencies_repository.get_currencies()
            
            return [
                convert_currency_document_to_entity(currency) 
                for currency in currencies
            ]
        except ApplicationException as exception:
            raise exception
        
@dataclass
class CreateNewCurrencySchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if not request.body:
            raise CurrencyNotFoundException()
        
        required_fields = ["name", "code", "sign"]
        missing_fields = [field for field in required_fields if field not in request.body]

        if missing_fields:
            raise RequiredFieldException()
        
    
    def parse_request(request: HTTPRequest, currencies_repository: BaseCurrenciesRepository) -> Currency:
        
        try:
            CreateNewCurrencySchema.check_request(request)
            
            currency_data = {
                "fullname": request.body["name"][0],
                "code": request.body["code"][0],
                "sign": request.body["sign"][0]
            }
            
            currency: Currency = convert_currency_document_to_entity(currency_data) 
            
            existing_currency = currencies_repository.get_currency_by_code(currency_data["code"])
            if existing_currency:
                raise CurrencyAlreadyExistsException()
                
            currencies_repository.add_currency(currency)
            
            return currency_data
            
        except ApplicationException as exception:
            raise exception
        
    
@dataclass
class CurrencyDetailSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 2:
            return RequiredFieldException()
    
    def parse_request(request: HTTPRequest, currencies_repository: BaseCurrenciesRepository) -> Iterable[Currency]:
        
        try:
            CurrencyDetailSchema.check_request(request)
            
            currency_code = request.parts[1]
            currency: Currency = currencies_repository.get_currency_by_code(currency_code)
            
            return convert_currency_document_to_entity(currency)
        except ApplicationException as exception:
            raise exception
        
    

    
