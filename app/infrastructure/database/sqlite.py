from dataclasses import dataclass, field
from logging import Logger
import sqlite3

from domain.exceptions.base import ApplicationException
from infrastructure.database.base import BaseDatabase
from infrastructure.exceptions.database import ConnectionFailedException, InitQueryExecutedFailedException, QueryExecutedFailedException
from infrastructure.logger.base import ILogger
from settings.config import Settings

@dataclass
class SQLiteDatabase(BaseDatabase):

    path: str = field(kw_only=True)
    logger: ILogger = field(default=Logger, kw_only=True)
    _is_connected: bool = field(default=False)

    def init(self, init_path: str):
        try:
            with open(init_path, "r") as f:
                init_query = f.read()
                self.cursor.executescript(init_query)
                self.logger.info('Инициализция прошла успешно')
        except ApplicationException as exception:
            self.logger.error(exception.message)
            raise InitQueryExecutedFailedException()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            self._is_connected = True
            self.logger.info('Соединение с базой данных успешно выполнена')
        except ApplicationException as exception:
            self.logger.error(exception.message)
            raise ConnectionFailedException()

    def close(self):
        self.connection.close()

    def execute(self, query: str):
        try:
            self.cursor = self.cursor.execute(query)
            self.logger.info('Запрос успешно выполнен')
            return self.cursor
        except ApplicationException as exception:
            self.logger.error(exception.message)
            raise QueryExecutedFailedException(query)
            
    @property
    def is_open(self):
        return self._is_connected


def sqlite_database_build() -> BaseDatabase:
    database: BaseDatabase = SQLiteDatabase()
    
    try:
        database.connect(path=Settings.DB_PATH)
        database.init(Settings.DB_INIT_PATH)
        
        return database
    except ApplicationException as exception:
        raise ApplicationException