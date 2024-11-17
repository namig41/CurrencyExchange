import sqlite3
from dataclasses import (
    dataclass,
    field,
)
from functools import lru_cache

from infrastructure.database.base import BaseDatabase
from infrastructure.exceptions.database import (
    ConnectionFailedException,
    InitQueryExecutedFailedException,
    QueryExecutedFailedException,
)
from infrastructure.logger.base import ILogger
from infrastructure.logger.logger import create_logger_dependency

from domain.exceptions.base import ApplicationException
from settings.config import Settings


@dataclass
class SQLiteDatabase(BaseDatabase):

    path: str = field(kw_only=True)
    logger: ILogger = field(default_factory=create_logger_dependency, kw_only=True)
    _is_connected: bool = field(default=False)

    def init(self, init_path: str):
        try:
            with open(init_path) as f:
                init_query = f.read()
                self.cursor.executescript(init_query)
                self.logger.info("Инициализция прошла успешно")
        except sqlite3.DatabaseError:
            raise InitQueryExecutedFailedException()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.path, check_same_thread=False)
            self.cursor = self.connection.cursor()
            self._is_connected = True
            self.logger.info("Соединение с базой данных успешно выполнена")
        except sqlite3.DatabaseError:
             raise ConnectionFailedException()

    def close(self):
        self.connection.close()

    def execute(self, query: str, *args):
        try:
            self.cursor = self.cursor.execute(query, args)
            self.logger.info("Запрос успешно выполнен")
            return self.cursor
        except sqlite3.DatabaseError:
            raise QueryExecutedFailedException(query)

    @property
    def is_open(self):
        return self._is_connected


@lru_cache
def sqlite_database_factory() -> BaseDatabase:
    database: BaseDatabase = SQLiteDatabase(path=Settings.DB_PATH)

    try:
        database.connect()
        database.init(Settings.DB_INIT_PATH)
        return database
    except ApplicationException as exception:
        logger: ILogger = create_logger_dependency()
        logger.error(exception.message)
        raise exception
