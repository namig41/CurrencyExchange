from dataclasses import dataclass, field
from application.router.base import BaseRouter
from application.schema.http.request import HTTPRequest
from application.schema.http.response import HTTPResponse
from application.schema.http.response_common import SuccessResponse
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
            return HTTPResponse(status_code=exception.code, data={"message": exception.message})
        return SuccessResponse(data=currency) 

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        ...

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        ...
