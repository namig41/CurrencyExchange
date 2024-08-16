from storage.database import DataBase
import sqlite3


class SQLiteDatabase(DataBase):

    is_connected = False

    def __init__(self, path: str = "database/db.db"):
        self.path = path

    def init(self, path: str = "database/init.sql"):
        with open(path, "r") as f:
            query_init = f.read()
            self.cur.executescript(query_init)

    def open(self):
        if not self.is_connected:
            self.con = sqlite3.connect(self.path)
            self.cur = self.con.cursor()
            self.is_connected = True

    def close(self):
        self.con.close()

    def execute(self, query: str):
        return self.cur.execute(query)
    
    def is_open(self):
        return self.is_connected
    

sqllite_database = SQLiteDatabase()
sqllite_database.open()