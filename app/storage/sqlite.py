from storage.database import DataBase

import sqlite3

class SQLiteDatabase(DataBase):

    def __init__(self, path = "database/db.db"):
        self.path = path

    def init(self, path = "database/init.sql"):
        with open(path, "r") as f:
            query_init = f.read()
            self.cur.executescript(query_init)

    def connect(self):
        self.con = sqlite3.connect(self.path)
        self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def execute(self, query):
        return self.cur.execute(query)