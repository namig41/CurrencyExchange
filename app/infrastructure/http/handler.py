from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Callable

import json

from app.infrastructure.router.currencies_router import CurrenciesRouter
from app.infrastructure.router.currency_router import CurrencyRouter
from app.infrastructure.router.exchange_rates_router import ExchangeRatesRouter
from app.infrastructure.router.exchange_rate_router import ExchangeRateRouter
from app.infrastructure.router.exchange_router import ExchangeRouter

from app.infrastructure.http.request.http_request import HTTPRequest
from app.infrastructure.http.response.http_response import HTTPResponse

from app.infrastructure.http.response.common_error import NotFound

class HTTPHandler(BaseHTTPRequestHandler):

    routers = [
        CurrenciesRouter(),
        CurrencyRouter(),
        ExchangeRatesRouter(),
        ExchangeRateRouter(),
        ExchangeRouter()
    ]

    def _set_headers(self, status_code=200, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def _requset_handler(self, request: HTTPRequest, callable: Callable[[HTTPRequest], HTTPResponse]) -> HTTPResponse:
        uri: list = request.parts[0]
        response: HTTPResponse = NotFound()
        for router in self.routers:
            if uri == router.prefix:
                response = callable(request)
                break

        return response

    def do_GET(self):
        request = HTTPRequest(self.path)
        request.parse(self.headers, self.rfile)

        uri: list = request.parts[0]
        response = NotFound()
        for router in self.routers:
            if uri == router.prefix:
                response = router.handle_get(request)
                break

        self._requset_handler(request, router.handle_get)

        self.do_response(response)

    def do_POST(self):
        request = HTTPRequest(self.path)
        request.parse(self.headers, self.rfile)

        uri = request.parts[0]
        response = NotFound()
        for router in self.routers:
            if uri == router.prefix:
                response = router.handle_post(request)
                break

        self.do_response(response)

    def do_PATCH(self):
        request = HTTPRequest(self.path)
        request.parse(self.headers, self.rfile)

        uri = request.parts[0]
        response = NotFound()
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