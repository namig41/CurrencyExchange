from dataclasses import dataclass, field
from http.client import HTTPResponse
from application.schema.http.response_success import SuccessResponse
from application.schema.router.exchange import ExchageConvertSchema
from domain.exceptions.base import ApplicationException
from infrastructure.dao.exchange_rates import ExchangeRatesDAO
from infrastructure.dao.currencies import CurrenciesDAO

from application.router.base import BaseRouter
from application.http.request.http_request import HTTPRequest
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.sqlite import sqlite_currencies_repository_factory, sqlite_exchange_rates_repository_factory

@dataclass
class ExchangeRouter(BaseRouter):

    prefix: str = field(default="exchange")
    currencies_repository: BaseCurrenciesRepository = field(default_factory=sqlite_currencies_repository_factory)
    exchange_rates_repository: BaseExchangeRatesRepository = field(default_factory=sqlite_exchange_rates_repository_factory)

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        try:
            exchange_rate = ExchageConvertSchema.parse_request(request,
                                                              self.currencies_repository,
                                                              self.exchange_rates_repository)    
        except ApplicationException as exception:
            return HTTPResponse(status_code=exception.code, data=exception.message)
        return SuccessResponse(data=exchange_rate) 
    
    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        ...

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        ...
