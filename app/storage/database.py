from abc import ABC, abstractmethod

class DataBase(ABC):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    @abstractmethod
    def init(self, path):
        pass

    @abstractmethod
    def open(self, path):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    @abstractmethod
    def is_open(self):
        pass

    