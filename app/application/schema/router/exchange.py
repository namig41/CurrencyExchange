from dataclasses import dataclass

from application.exceptions.http.exchange import ExchangeNotFoundException
from application.exceptions.http.exchange_rate import ExchangeRateMissingException
from application.schema.http.request import HTTPRequest
from application.router import exchange_rate
from application.schema.router.base import BaseSchema
from application.schema.router.exchange_rate import ExchageRateDetailSchema
from domain.entities.exchange_rate import ExchangeRate
from domain.exceptions.base import ApplicationException
from infrastructure.repositories.base import BaseCurrenciesRepository, BaseExchangeRatesRepository
from infrastructure.repositories.converters import convert_exchange_entity_to_document, convert_exchange_rate_entity_to_document


# def forward_convert(self, request: HTTPRequest):
#         from_currency = self.dao_currencies.find_by(code=request.param["from"][0])
#         to_currency = self.dao_currencies.find_by(code=request.param["to"][0])

#         if not from_currency or not to_currency:
#             return

#         exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
#                                               TargetCurrencyId=to_currency["id"])
        
#         if not exchange_rate:
#             return

#         converted_amount = exchange_rate["rate"] * float(request.param["amount"][0])

#         exchange  = {"baseCurrency": from_currency,
#                  "targetCurrency": to_currency,
#                  "rate": exchange_rate["rate"],
#                  "amount": request.param["amount"][0],
#                  "convertedAmount": converted_amount
#         }

#         return SuccessResponse(exchange)
    

# def reverse_convert(self, request: HTTPRequest):

#         from_currency = self.dao_currencies.find_by(code=request.param["to"][0])
#         to_currency = self.dao_currencies.find_by(code=request.param["from"][0])

#         if not from_currency or not to_currency:
#             return

#         exchange_rate = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
#                                               TargetCurrencyId=to_currency["id"])
        
#         if not exchange_rate:
#             return 

#         converted_amount = exchange_rate["rate"] * 1 / float(request.param["amount"][0])

#         exchange  = {"baseCurrency": from_currency,
#                  "targetCurrency": to_currency,
#                  "rate": exchange_rate["rate"],
#                  "amount": request.param["amount"][0],
#                  "convertedAmount": converted_amount
#         }

#         return SuccessResponse(exchange)
    

# def cross_convert(self, request: HTTPRequest):

#         from_currency = self.dao_currencies.find_by(code=request.param["to"][0])
#         to_usd_currency = self.dao_currencies.find_by(code="USD")
#         to_currency = self.dao_currencies.find_by(code=request.param["from"][0])

#         if not from_currency or not to_currency:
#             return CurrencyNotFoundError()

#         exchange_rate_1 = self.dao_exchange_rate.find_by(BaseCurrencyId=from_currency["id"],
#                                               TargetCurrencyId=to_usd_currency["id"])
        
#         exchange_rate_2 = self.dao_exchange_rate.find_by(BaseCurrencyId=to_usd_currency["id"],
#                                               TargetCurrencyId=to_currency["id"])
        
#         if not exchange_rate_1 or not exchange_rate_2:
#             return ExchangeNotFoundError()

#         converted_amount = exchange_rate_1["rate"] * float(request.param["amount"][0])
#         converted_amount = exchange_rate_2["rate"] * float(converted_amount)

#         exchange  = {"baseCurrency": from_currency,
#                  "targetCurrency": to_currency,
#                  "rate": {exchange_rate_1["rate"], exchange_rate_2["rate"]},
#                  "amount": request.param["amount"][0],
#                  "convertedAmount": converted_amount
#         }

#         return SuccessResponse(exchange)
    
@dataclass
class ExchageConvertSchema(BaseSchema):
    
    def check_request(request: HTTPRequest):
        if len(request.parts) != 1:
            return ExchangeNotFoundException()
        
        required_fields = ["from", "to", "amount"]
        missing_fields = [field for field in required_fields if field not in request.param]

        if missing_fields:
            raise ExchangeNotFoundException() 
        
    
    def parse_request(
        request: HTTPRequest,
        exchange_rates_repository: BaseExchangeRatesRepository
    ) -> ExchangeRate: 
        try:
            ExchageConvertSchema.check_request(request)
            
            base_code = request.param["from"][0]
            target_code = request.param["to"][0]
            amount = float(request.param["amount"][0])
            
            exchange_rate = exchange_rates_repository.get_exchange_rate_by_codes(base_code, target_code)
            converted_amount = 0
            
            return convert_exchange_entity_to_document(exchange_rate, amount, converted_amount)
        except ApplicationException as exception:
            raise exception
        