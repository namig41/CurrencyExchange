from domain.services.conversion_service import ConversionService


class CurrencyConversionService:
    def __init__(self, conversion_service: ConversionService, exchange_rate_repository: ExchangeRateRepository):
        ...
