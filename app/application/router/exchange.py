from dataclasses import dataclass, field
from http.client import HTTPResponse
from application.schema.http.response_success import SuccessResponse
from application.schema.router.exchange import ExchageDetailSchema
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

        # required_fields = ["from", "to", "amount"]
        # missing_fields = [field for field in required_fields if field not in request.param]

        # if missing_fields:
        #     return RequiredFieldMissingError()

        # return (self.forward_convert(request) or
        #         self.reverse_convert(request) or
        #         self.cross_convert(request) or
        #         ExchangeNotFoundError())
        
        try:
            exchange_rate = ExchageDetailSchema.parse_request(request,
                                                              self.currencies_repository,
                                                              self.exchange_rates_repository)    
        except ApplicationException as exception:
            return HTTPResponse(status_code=exception.code, data=exception.message)
        return SuccessResponse(data=exchange_rate) 
    
    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        ...

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        ...
