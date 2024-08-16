from router.base import BaseRouter

from request.http_request import HTTPRequest
from response.http_response import HTTPResponse  

from currencies.dao import CurrenciesDAO

from currency.errors import (CurrencyNotFoundError,
                               CurrencyAlreadyExistsError,
                               DatabaseError,
                               RequiredFieldMissingError)

from response.base_success import SuccessResponse


class CurrenciesRouter(BaseRouter):

    def __init__(self):
        self.prefix = "currencies"
        self.dao = CurrenciesDAO()

    def handle_get(self, request: HTTPRequest) -> HTTPResponse:       
        if len(request.parts) != 1:
            return RequiredFieldMissingError()

        currencies = self.dao.find_all()
        return SuccessResponse(currencies)        

    def handle_post(self, request: HTTPRequest) -> HTTPResponse:
        if not request.body:
            return CurrencyNotFoundError()
        
        required_fields = ["name", "code", "sign"]
        missing_fields = [field for field in required_fields if field not in request.body]

        if missing_fields:
            return RequiredFieldMissingError()
        
        currency_data = {
            "FullName": request.body["name"][0],
            "Code": request.body["code"][0],
            "Sign": request.body["sign"][0]
        }

        existing_currency = self.dao.find_by(code=currency_data["Code"])
        if existing_currency:
            return CurrencyAlreadyExistsError()
        
        self.dao.insert(currency_data)
        currency = self.dao.find_by(code=currency_data["Code"])

        return SuccessResponse(currency)

    def handle_patch(self, request: HTTPRequest) -> HTTPResponse:
        pass