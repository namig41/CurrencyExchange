from dao.base import BaseDao

class DAO(BaseDao):
    """
        Класс, который реализует базовые манипуляции с БД
    """
    
    def __init__(self):
        self.table_name = None
        self.database = None
    
    def find_by_id(self, id):
        query = "SELECT * FROM %s WHERE id = %s" % (self.table_name, id)
        return self.database.execute_query(query)

    def find_all(self):
        query = "SELECT * FROM %s" % (self.table_name)
        return self.database.execute_query(query)

    def insert(self, data):
        query =  "INSERT INTO  %s (%s) VALUES (%s)"  %  (self.table_name, ",".join(data.keys()), ":".join(data.values()))
        return self.database.execute_query(query)

    def update(self, data):
        query  =   "UPDATE  %s SET %s WHERE id = %s"  %  (self.table_name,  ",".join(data.keys()), id)
        return self.database.execute_query(query)

    def delete(self, id):
        query =   "DELETE FROM  %s WHERE id  =  %s"  %  (self.table_name, id)
        return self.database.execute_query(query)
