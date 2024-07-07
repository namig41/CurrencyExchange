from abc import ABC, abstractmethod

class DataBase(ABC):
    
    @abstractmethod
    def init(self, path):
        pass

    @abstractmethod
    def connect(self, path):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute(self, query):
        pass

    