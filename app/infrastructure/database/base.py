from abc import ABC, abstractmethod, ABCMeta

class BaseDatabase(ABC):
    
    @abstractmethod
    def init(self, path: str):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def execute(self, query: str):
        pass

    @abstractmethod
    def is_open(self):
        pass

    