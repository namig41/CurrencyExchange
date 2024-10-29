from dataclasses import dataclass
from typing import Iterable
from application.exceptions.http.common import RequiredFieldException
from application.schema.http.request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.currency import Currency
from domain.exceptions.base import ApplicationException
from infrastructure.repositories.base import BaseCurrenciesRepository
from infrastructure.repositories.converters import convert_currency_document_to_entity, convert_currency_entity_to_document
  
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
            
            return convert_currency_entity_to_document(currency)
        except ApplicationException as exception:
            raise exception
        
    

    
