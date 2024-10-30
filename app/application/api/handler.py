from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler

import json

from application.http.request.parse import ParseHTTPRequestStrategy, ParseRequest
from application.router.base import BaseRouter
from application.router.currencies import CurrenciesRouter
from application.router.currency import CurrencyRouter
from application.router.exchange_rates import ExchangeRatesRouter
from application.router.exchange_rate import ExchangeRateRouter
from application.router.exchange import ExchangeRouter

from application.schema.http.request import HTTPRequest
from application.schema.http.response import HTTPResponse
from application.schema.http.response_common import NotFoundResponse


class HTTPHandlerConfigMixin:
    routers: list[BaseRouter] = [
            CurrenciesRouter(),
            CurrencyRouter(),
            ExchangeRatesRouter(),
            ExchangeRateRouter(),
            ExchangeRouter()
        ]
    
    parse_strategy: ParseHTTPRequestStrategy = ParseRequest()
    
class HTTPHandler(HTTPHandlerConfigMixin, BaseHTTPRequestHandler):

    def do_GET(self):
        request = self.parse_strategy.parse(self.path, self.headers, self.rfile)

        uri = request.parts[0]
        response = NotFoundResponse()
        for router in self.routers:
            if uri == router.prefix:
                response = router.handle_get(request)
                break

        self.do_response(response)

    def do_POST(self):
        request = self.parse_strategy.parse(self.path, self.headers, self.rfile)

        uri = request.parts[0]
        response = NotFoundResponse()     
        for router in self.routers:
            if uri == router.prefix:
                response = router.handle_post(request)
                break

        self.do_response(response)

    def do_PATCH(self):
        request = self.parse_strategy.parse(self.path, self.headers, self.rfile)

        uri = request.parts[0]
        response = NotFoundResponse()
        for router in self.routers:
            if uri == router.prefix:
                response = router.handle_patch(request)
                break

        self.do_response(response)

    def do_response(self, response: HTTPResponse):
        self.send_response(response.status_code)
        self.send_header("Content-type", 'text/json')
        self.end_headers()

        response_content = json.dumps(response.data)
        self.wfile.write(response_content.encode())