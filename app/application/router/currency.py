from dataclasses import dataclass, field
from http.client import HTTPResponse
from application.router.base import BaseRouter
from application.http.request.http_request import HTTPRequest
from application.schema.http.response_success import SuccessResponse
from application.schema.router.currency import CurrencyDetailSchema
from domain.exceptions.base import ApplicationException
from infrastructure.dao.currencies import CurrenciesDAO
from infrastructure.repositories.base import BaseCurrenciesRepository
from infrastructure.repositories.sqlite import sqlite_currencies_repository_factory

@dataclass
class CurrencyRouter(BaseRouter):
        
    prefix: str = field(default="currency")
    currencies_repository: BaseCurrenciesRepository = field(default_factory=sqlite_currencies_repository_factory)

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        try:
            currency = CurrencyDetailSchema.parse_request(request, self.currencies_repository)    
        except ApplicationException as exception:
            return HTTPResponse(status_code=exception.code, data=exception.message)
        return SuccessResponse(data=currency) 

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        pass

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass
