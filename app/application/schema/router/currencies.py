from dataclasses import dataclass
from typing import Iterable
from application.exceptions.http.common import RequiredFieldException
from application.exceptions.http.currency import CurrencyAlreadyExistsException, CurrencyNotFoundException
from application.http.request.http_request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.currency import Currency
from domain.exceptions.base import ApplicationException
from infrastructure.repositories.base import BaseCurrenciesRepository
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
                convert_currency_entity_to_document(currency) 
                for currency in currencies
            ]
        except ApplicationException as exception:
            raise exception
        
@dataclass
class CreateNewCurrencySchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if not request.body:
            raise RequiredFieldException()
        
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
            
            # currency: Currency = convert_currency_document_to_entity(currency_data)

            # TODO: необходимо вынести в конвертацию             
            currency: Currency = Currency(
                code=currency_data['code'],
                fullname=currency_data['fullname'],
                sign=currency_data['sign'],
            )
            
            # TODO: Оптимизировать количество запросов
                    
            if currencies_repository.get_currency_by_code(currency_data["code"]):
                raise CurrencyAlreadyExistsException()
                
            currencies_repository.add_currency(currency)
            
            inserted_currency: Currency = currencies_repository.get_currency_by_code(currency_data["code"])
            
            return convert_currency_entity_to_document(inserted_currency)
            
        except ApplicationException as exception:
            raise exception