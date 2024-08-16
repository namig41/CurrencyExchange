from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from env import Settings

from currencies.router import CurrenciesRouter
from currency.router import CurrencyRouter
from exchange_rates.router import ExchangeRatesRouter
from exchange_rate.router import ExchangeRateRouter
from exchange.router import ExchangeRouter

from requestschema.http_request import HTTPRequest
from requestschema.http_response import HTTPResponse

from response.common_error import NotFound

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

        uri = request.parts[0]
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
    
    
def run(server_class=HTTPServer, handler_class=HTTPHandler, hostname='127.0.0.1', port=8080):
    server_address = (hostname, port)
    websererver = server_class(server_address, handler_class)
    print(f'Сервер запущен {hostname}:{port}...')

    try:
        websererver.serve_forever()
    except KeyboardInterrupt:
        pass

    websererver.server_close()
    print("Сервер остановлен.")



if __name__ == "__main__":
    run()
