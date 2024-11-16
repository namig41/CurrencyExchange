from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Any

from infrastructure.database.base import BaseDatabase


class BaseDAO(ABC):
    """
    Абстрактный класс, который реализует базовые манипуляции с БД
    """

    @abstractmethod
    def find_by_id(self, record_id: int) -> dict | None: ...

    @abstractmethod
    def find_by(self, **kwargs) -> dict | None: ...

    @abstractmethod
    def find_all(self) -> list[dict[Any, Any]]: ...

    @abstractmethod
    def insert(self, data) -> None: ...

    @abstractmethod
    def update(self, data) -> None: ...

    @abstractmethod
    def delete(self, **kwargs) -> None: ...


@dataclass
class DAO(BaseDAO):
    """
    Класс, который реализует базовые манипуляции с БД
    """

    database: BaseDatabase
    table_name: str

    def find_by_id(self, item_id: int) -> dict | None:
        query = f"SELECT * FROM {self.table_name} WHERE id = {item_id}"
        result = self.database.execute(query)

        if result:
            columns = [desc[0].lower() for desc in result.description]
            data = result.fetchone()
            return dict(zip(columns, data))

        return None

    def find_by(self, **kwargs) -> dict | None:
        conditions = " AND ".join(
            [
                f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}"
                for key, value in kwargs.items()
            ],
        )
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
        values = ",".join(
            "'" + str(value) + "'" if isinstance(value, str) else str(value)
            for value in data.values()
        )

        query = f"INSERT INTO  {self.table_name} ({columns}) VALUES ({values})"
        self.database.execute(query)

    def update(self, data: dict, **kwargs) -> None:
        values = ", ".join(
            [
                f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}"
                for key, value in data.items()
            ],
        )

        conditions = " AND ".join(
            [
                f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}"
                for key, value in kwargs.items()
            ],
        )

        query = f"UPDATE {self.table_name} SET {values} WHERE {conditions}"
        print(query)
        self.database.execute(query)

    def delete(self, **kwargs) -> None:
        conditions = " AND ".join(
            [
                f"{key}='{value}'" if isinstance(value, str) else f"{key}={value}"
                for key, value in kwargs.items()
            ],
        )

        query = f"DELETE FROM {self.table_name} WHERE id  =  {conditions}"
        self.database.execute(query)
