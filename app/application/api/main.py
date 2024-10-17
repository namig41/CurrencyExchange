from http.server import HTTPServer, BaseHTTPRequestHandler

from application.api.handler import HTTPHandler
from settings.config import Settings


def run(
    server_class=HTTPServer,
    handler=HTTPHandler,
    hostname=Settings.SERVER_HOST,
    port=Settings.SERVER_PORT
    ):
    
    server_address = (hostname, port)
    web_server = server_class(server_address, handler)
    print(f'Сервер запущен {hostname}:{port}...')

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Сервер остановлен.")


if __name__ == "__main__":
    run()
