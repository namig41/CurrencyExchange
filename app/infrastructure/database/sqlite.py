from dataclasses import dataclass
import sqlite3

from infrastructure.database.database import IDataBase

@dataclass
class SQLiteDatabase(IDataBase):

    is_connected: bool = False
    path: str = "database/db.db"

    def init(self, path: str = "database/init.sql"):
        with open(path, "r") as f:
            query_init = f.read()
            self.cursor.executescript(query_init)

    def connect(self):
        if not self.is_connected:
            self.connection = sqlite3.connect(self.path)
            self.cursor = self.connection.cursor()
            self.is_connected = True

    def close(self):
        self.connection.close()

    def execute(self, query: str):
        return self.cursor.execute(query)
    
    def is_open(self):
        return self.is_connected
