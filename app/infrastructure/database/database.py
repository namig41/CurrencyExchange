from abc import ABC, abstractmethod, ABCMeta

class SingletonMeta(ABCMeta):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DataBase(ABC, metaclass=SingletonMeta):
    
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

    