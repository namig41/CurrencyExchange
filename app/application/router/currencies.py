from dataclasses import dataclass, field
from http.client import HTTPResponse
from typing import Iterable
from application.router.base import BaseRouter

from application.http.request.http_request import HTTPRequest

from application.schema.http.response_success import SuccessResponse
from application.schema.router.currency import CreateNewCurrencySchema, CurrenciesDetailSchema
from domain.entities.currency import Currency
from domain.exceptions.base import ApplicationException
from infrastructure.dao.currencies import CurrenciesDAO

from infrastructure.repositories.base import BaseCurrenciesRepository
from infrastructure.repositories.sqlite import sqlite_currencies_repository_factory

@dataclass
class CurrenciesRouter(BaseRouter):

    prefix: str = field(default="currencies")
    currencies_repository: BaseCurrenciesRepository = field(default_factory=sqlite_currencies_repository_factory)

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        try:
            currencies: Iterable[Currency] = CurrenciesDetailSchema.parse_request(request, self.currencies_repository)    
        except ApplicationException as exception:
            return HTTPResponse(status_code=exception.code, data=exception.message)
        
        return SuccessResponse(data=currencies)        

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        try:
            currency: Currency = CreateNewCurrencySchema.parse_request(request, self.currencies_repository)    
        except ApplicationException as exception:
            return HTTPResponse(status_code=exception.code, data=exception.message)
        
        return SuccessResponse(data=currency)    


    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass
