from http.server import HTTPServer, BaseHTTPRequestHandler

from application.api.handler import HTTPHandler


def run(server_class=HTTPServer, handler=HTTPHandler, hostname='0.0.0.0', port=8000):
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
