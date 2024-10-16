from dataclasses import dataclass
import logging

from infrastructure.logger.base import ILogger

@dataclass
class Logger(ILogger):
    
    _logger: logging.Logger
    _error_logger: logging.Logger

    def info(self, message: str) -> None:
        self._logger.info(message)

    def error(self, message: str) -> None:
        self._error_logger.error(message)

    def debug(self, message: str) -> None:
        self._logger.debug(message)
