from dataclasses import dataclass
from decimal import Decimal

from infrastructure.repositories.base import BaseExchangeRatesRepository
from infrastructure.repositories.converters import (
    convert_exchange_entity_to_document,
    convert_exchanges_entity_to_document,
)

from application.exceptions.http.exchange import ExchangeNotFoundException
from application.schema.http.request import HTTPRequest
from application.schema.router.base import BaseSchema
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from domain.services.currency_exchange_service import (
    cross_exchange,
    exchange,
    reverse_exchange,
)


@dataclass
class ExchageConvertSchema(BaseSchema):

    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            return ExchangeNotFoundException()

        required_fields = ["from", "to", "amount"]
        missing_fields = [
            field for field in required_fields if field not in request.param
        ]

        if missing_fields:
            raise ExchangeNotFoundException()

    def parse_request(
        request: HTTPRequest,
        exchange_rates_repository: BaseExchangeRatesRepository,
    ) -> ExchangeRate:
        try:
            ExchageConvertSchema.check_request(request)

            base_code = request.param["from"][0]
            target_code = request.param["to"][0]
            amount = Decimal(request.param["amount"][0])

            conversion_result = exchange(
                base_code,
                target_code,
                amount,
                exchange_rates_repository,
            )
            if conversion_result:
                exchange_rate, converted_amount = conversion_result
                return convert_exchange_entity_to_document(
                    exchange_rate,
                    amount,
                    converted_amount,
                )

            conversion_result = reverse_exchange(
                base_code,
                target_code,
                amount,
                exchange_rates_repository,
            )
            if conversion_result:
                exchange_rate, converted_amount = conversion_result
                return convert_exchange_entity_to_document(
                    exchange_rate,
                    amount,
                    converted_amount,
                )

            conversion_result = cross_exchange(
                base_code,
                target_code,
                amount,
                exchange_rates_repository,
            )
            if conversion_result:
                exchange_rates, converted_amount = conversion_result
                return convert_exchanges_entity_to_document(
                    exchange_rates,
                    amount,
                    converted_amount,
                )

            raise ExchangeNotFoundException()

        except ApplicationException as exception:
            raise exception
