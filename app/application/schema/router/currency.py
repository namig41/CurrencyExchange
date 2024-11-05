from dataclasses import dataclass
from typing import Iterable

from infrastructure.repositories.base import BaseCurrenciesRepository
from infrastructure.repositories.converters import convert_currency_entity_to_document

from application.exceptions.http.common import RequiredFieldMissingException
from application.exceptions.http.currency import CurrencyNotFoundException
from application.schema.http.request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.currency import Currency
from domain.exceptions.base import ApplicationException


@dataclass
class CurrencyDetailSchema(BaseSchema[Iterable[Currency]]):

    def check_request(request: HTTPRequest):
        if len(request.parts) != 2:
            raise RequiredFieldMissingException()

    def parse_request(
        request: HTTPRequest,
        currencies_repository: BaseCurrenciesRepository,
    ) -> Iterable[Currency]:

        try:
            CurrencyDetailSchema.check_request(request)

            currency_code = request.parts[1]
            currency: Currency = currencies_repository.get_currency_by_code(
                currency_code,
            )

            if currency is None:
                raise CurrencyNotFoundException()

            return convert_currency_entity_to_document(currency)
        except ApplicationException as exception:
            raise exception
