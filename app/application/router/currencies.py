from dataclasses import (
    dataclass,
    field,
)
from typing import Iterable

from infrastructure.repositories.base import BaseCurrenciesRepository
from infrastructure.repositories.sqlite import sqlite_currencies_repository_factory

from application.router.base import BaseRouter
from application.schema.http.request import HTTPRequest
from application.schema.http.response import HTTPResponse
from application.schema.http.response_common import (
    NotFoundResponse,
    SuccessResponse,
)
from application.schema.router.currencies import (
    CreateNewCurrencySchema,
    CurrenciesDetailSchema,
)
from domain.entities.currency import Currency
from domain.exceptions.base import ApplicationException


@dataclass
class CurrenciesRouter(BaseRouter):

    prefix: str = field(default="currencies")
    currencies_repository: BaseCurrenciesRepository = field(
        default_factory=sqlite_currencies_repository_factory,
    )

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        try:
            currencies: Iterable[Currency] = CurrenciesDetailSchema.parse_request(
                request,
                self.currencies_repository,
            )
        except ApplicationException as exception:
            return HTTPResponse(
                status_code=exception.code,
                data={"message": exception.message},
            )

        return SuccessResponse(data=currencies)

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        try:
            currency: Currency = CreateNewCurrencySchema.parse_request(
                request,
                self.currencies_repository,
            )
        except ApplicationException as exception:
            return HTTPResponse(
                status_code=exception.code,
                data={"message": exception.message},
            )

        return SuccessResponse(data=currency)

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        return NotFoundResponse()
