from abc import ABC, abstractmethod

class BaseDAO(ABC):
    """
        Абстрактный класс, который реализует базовые манипуляции с БД
    """
    
    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_by(self, **kwargs) -> dict | None:
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def insert(self, data):
        pass

    @abstractmethod
    def update(self, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass
