from abc import ABC, abstractmethod, ABCMeta

class BaseDatabase(ABC):
    
    @abstractmethod
    def init(self, path: str):
        ...

    @abstractmethod
    def connect(self):
        ...

    @abstractmethod
    def close(self):
        ...

    @abstractmethod
    def execute(self, query: str):
        ...

    @abstractmethod
    def is_open(self):
        ...

    