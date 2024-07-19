from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from currencies.router import CurrenciesRouter
from exchange_rates.router import ExchangeRatesRouter
from exchange.router import ExchangeRouter

from handlers.http_request import HTTPRequest
from handlers.http_response import HTTPResponse

class HTTPHandler(BaseHTTPRequestHandler):

    routers = [
        CurrenciesRouter(),
        ExchangeRatesRouter(),
        ExchangeRouter()
    ]

    def _set_headers(self, status_code=200, content_type='text/html'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        request = HTTPRequest(self.path)
        request.parse(self.headers, self.rfile)
        
        response = HTTPResponse(404, "Not Found")
        for router in self.routers:
            if self.path.startswith(router.prefix):
                response = router.handle_get(request)
                break

        self.do_response(response)

    def do_POST(self):
        request = HTTPRequest(self.path)
        request.parse(self.headers, self.rfile)  

        print(request)    

        response = HTTPResponse(404, "Not Found")
        for router in self.routers:
            if self.path.startswith(router.prefix):
                response = router.handle_post(request)
                break

        self.do_response(response)

    def do_PATCH(self):
        request = HTTPRequest(self.path)
        request.parse(self.headers, self.rfile)

        response = HTTPResponse(404, "Not Found")
        for router in self.routers:
            if self.path.startswith(router.prefix):
                response = router.handle_patch(request)
                break

        self.do_response(response)

    def do_response(self, response: HTTPResponse):
        self.send_response(response.status_code)
        self.send_header("Content-type", 'text/json')
        self.end_headers()

        response_content = json.dumps(response.data)
        self.wfile.write(response_content.encode())
    
    
def run(server_class=HTTPServer, handler_class=HTTPHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Сервер начал работу {port}...')
    httpd.serve_forever()



if __name__ == "__main__":
    run()
