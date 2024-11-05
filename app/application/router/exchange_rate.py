from dataclasses import (
    dataclass,
    field,
)

from infrastructure.repositories.base import (
    BaseCurrenciesRepository,
    BaseExchangeRatesRepository,
)
from infrastructure.repositories.sqlite import (
    sqlite_currencies_repository_factory,
    sqlite_exchange_rates_repository_factory,
)

from application.router.base import BaseRouter
from application.schema.http.request import HTTPRequest
from application.schema.http.response import HTTPResponse
from application.schema.http.response_common import (
    NotFoundResponse,
    SuccessResponse,
)
from application.schema.router.exchange_rate import (
    ExchageRateDetailSchema,
    ExchageRateUpdateSchema,
)
from domain.exceptions.base import ApplicationException


@dataclass
class ExchangeRateRouter(BaseRouter):

    prefix: str = field(default="exchangeRate")
    currencies_repository: BaseCurrenciesRepository = field(
        default_factory=sqlite_currencies_repository_factory,
    )
    exchange_rates_repository: BaseExchangeRatesRepository = field(
        default_factory=sqlite_exchange_rates_repository_factory,
    )

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:
        try:
            exchange_rate = ExchageRateDetailSchema.parse_request(
                request,
                self.exchange_rates_repository,
            )
        except ApplicationException as exception:
            return HTTPResponse(
                status_code=exception.code,
                data={"message": exception.message},
            )
        return SuccessResponse(data=exchange_rate)

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        return NotFoundResponse()

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        try:
            exchange_rate = ExchageRateUpdateSchema.parse_request(
                request,
                self.currencies_repository,
                self.exchange_rates_repository,
            )
        except ApplicationException as exception:
            return HTTPResponse(
                status_code=exception.code,
                data={"message": exception.message},
            )
        return SuccessResponse(data=exchange_rate)
