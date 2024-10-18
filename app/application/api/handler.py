from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Callable

import json

from application.router.currencies import CurrenciesRouter
from application.router.currency import CurrencyRouter
from application.router.exchange_rates import ExchangeRatesRouter
from application.router.exchange_rate import ExchangeRateRouter
from application.router.exchange import ExchangeRouter

from application.http.request.http_request import HTTPRequest
from application.http.response.http_response import HTTPResponse

from application.http.response.common_error import NotFound

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

    def do_GET(self):
        request = HTTPRequest(self.path)
        request.parse(self.headers, self.rfile)

        uri: list = request.parts[0]
        response = NotFound()
        for router in self.routers:
            if uri == router.prefix:
                response = router.handle_get(request)
                break

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