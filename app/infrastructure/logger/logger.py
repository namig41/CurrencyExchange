import logging
import sys
from dataclasses import dataclass
from functools import lru_cache
from typing import TextIO

from infrastructure.logger.base import ILogger


@dataclass
class Logger:

    logger: logging.Logger
    error_logger: logging.Logger

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str) -> None:
        self.error_logger.error(message)

    def debug(self, message: str) -> None:
        self.logger.debug(message)


def logger_factory(name: str, level: int, stream: TextIO) -> logging.Logger:
    """
    Factory to create a logging.Logger instance with the given name,
    log level and stream to write to.

    :param name: name of the logger
    :param level: logging level
    :param stream: stream to write log messages to
    :return: a new logging.Logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = logging.StreamHandler(stream=stream)

    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    if handler not in logger.handlers:
        logger.addHandler(handler)

    return logger


@lru_cache
def create_logger_dependency() -> ILogger:
    common_logger: logging.Logger = logger_factory(
        name="common",
        level=logging.INFO,
        stream=sys.stdout,
    )
    error_logger: logging.Logger = logger_factory(
        name="error",
        level=logging.ERROR,
        stream=sys.stderr,
    )
    return Logger(logger=common_logger, error_logger=error_logger)
