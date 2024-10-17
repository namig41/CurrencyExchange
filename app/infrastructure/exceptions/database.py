from dataclasses import dataclass

from infrastructure.exceptions.base import InfrastructureException

@dataclass
class ConnectionFailedException(InfrastructureException):
    @property
    def message(self):
        return 'Ошибка подключения к базе данных'
    
    
@dataclass
class QueryExecutedFailedException(InfrastructureException):
    query: str
    
    @property
    def message(self):
        return f'Ошибка при выполнения запроса {self.query}'
    
@dataclass
class InitQueryExecutedFailedException(InfrastructureException):    
    @property
    def message(self):
        return f'Ошибка при выполнения инициализация запроса'