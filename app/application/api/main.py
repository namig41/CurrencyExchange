from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import BaseServer

from application.api.handler import HTTPHandler
from infrastructure.logger.base import ILogger
from infrastructure.logger.logger import create_logger_dependency
from settings.config import Settings


def run(
    server_class: BaseServer = HTTPServer,
    handler: BaseHTTPRequestHandler = HTTPHandler,
    hostname: str = Settings.SERVER_HOST,
    port: str = Settings.SERVER_PORT,
    logger: ILogger = create_logger_dependency()
    ):
    
    server_address = (hostname, port)
    web_server = server_class(server_address, handler)
    
    logger.info(f'Сервер запущен {hostname}:{port}...')

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    
    logger.info('Сервер остановлен')


if __name__ == "__main__":
    run()
