from http.server import (
    BaseHTTPRequestHandler,
    HTTPServer,
)
from socketserver import BaseServer

from infrastructure.logger.base import ILogger
from infrastructure.logger.logger import create_logger_dependency

from application.api.handler import HTTPHandler
from settings.config import Settings


def run(
    server_class: BaseServer = HTTPServer,
    handler: BaseHTTPRequestHandler = HTTPHandler,
    hostname: str = Settings.SERVER_HOST,
    port: int = Settings.SERVER_PORT,
    logger: ILogger = create_logger_dependency(),
):

    server_address = (hostname, port)
    web_server = server_class(server_address, handler)

    logger.info(f"Сервер запущен {hostname}:{port}...")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        ...

    web_server.server_close()

    logger.info("Сервер остановлен")


if __name__ == "__main__":
    run()
