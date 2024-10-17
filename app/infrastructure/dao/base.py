from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any

from infrastructure.database.base import BaseDatabase

class BaseDAO(ABC):
    """
        Абстрактный класс, который реализует базовые манипуляции с БД
    """
    
    @abstractmethod
    def find_by_id(self, id: int):
        pass

    @abstractmethod
    def find_by(self, **kwargs) -> dict | None:
        pass

    @abstractmethod
    def find_all(self) -> list[dict[Any, Any]]:
        pass

    @abstractmethod
    def insert(self, data) -> None:
        pass

    @abstractmethod
    def update(self, data) -> None:
        pass

    @abstractmethod
    def delete(self, **kwargs) -> None:
        pass

@dataclass
class DAO(BaseDAO):
    """
        Класс, который реализует базовые манипуляции с БД
    """
    
    database: BaseDatabase
    table_name: str

    def find_by_id(self, id: int) -> dict | None:
        query = "SELECT * FROM %s WHERE id = %s" % self.table_name, id
        result = self.database.execute(query)

        if result:
            columns = [desc[0].lower() for desc in result.description]
            data = result.fetchone()
            return dict(zip(columns, data))

        return None

    def find_by(self, **kwargs) -> dict | None:
        conditions = " AND ".join(
            [f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}" for key, value in kwargs.items()])
        query = f"SELECT * FROM {self.table_name} WHERE {conditions}"

        result = self.database.execute(query)

        if result:
            columns = [desc[0].lower() for desc in result.description]
            data = result.fetchone()
            if not data:
                return None
            return dict(zip(columns, data))

        return None

    def find_all(self) -> list[dict[Any, Any]]:
        query = "SELECT * FROM %s" % self.table_name
        result = self.database.execute(query)

        columns = [desc[0].lower() for desc in result.description]
        rows = result.fetchall()

        results = [dict(zip(columns, row)) for row in rows]
        return results

    def insert(self, data: dict) -> None:
        columns = ",".join(data.keys())
        values = ",".join("'" + str(value) + "'" if isinstance(value, str) else str(value) for value in data.values())

        query = "INSERT INTO  %s (%s) VALUES (%s)" % self.table_name, columns, values
        self.database.execute(query)

    def update(self, data: dict, **kwargs) -> None:
        columns = ",".join(data.keys())
        values = ",".join("'" + str(value) + "'" if isinstance(value, str) else str(value) for value in data.values())
        conditions = " AND ".join(
            [f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}" for key, value in kwargs.items()])

        query = "UPDATE %s SET %s WHERE %s" % self.table_name, columns, values, conditions
        self.database.execute(query)

    def delete(self, **kwargs) -> None:
        conditions = " AND ".join(
            [f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}" for key, value in kwargs.items()])

        query = "DELETE FROM  %s WHERE id  =  %s" % self.table_name, conditions
        self.database.execute(query)