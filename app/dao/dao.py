from dao.base import BaseDAO


class DAO(BaseDAO):
    """
        Класс, который реализует базовые манипуляции с БД
    """
    
    def __init__(self):
        self.table_name = None

    
    def find_by_id(self, id) -> dict:
        query = "SELECT * FROM %s WHERE id = %s" % (self.table_name, id)
        result = self.database.execute(query)

        if result:
            columns = [desc[0] for desc in result.description]
            data = result.fetchone()
            return dict(zip(columns, data))
    
        return None
    
    def find_by_name(self, name) -> dict:
        query = "SELECT * FROM %s WHERE Code = '%s'" % (self.table_name, name)
        result = self.database.execute(query)

        if result:
            columns = [desc[0] for desc in result.description]
            data = result.fetchone()
            print(columns, data)
            return dict(zip(columns, data))
    
        return None

    def find_all(self) -> dict:
        query = "SELECT * FROM %s" % (self.table_name)
        result = self.database.execute(query)
    
        columns = [desc[0] for desc in result.description]
        rows = result.fetchall()
        
        results = [dict(zip(columns, row)) for row in rows]
        return results

    def insert(self, data: dict):
        query =  "INSERT INTO  %s (%s) VALUES (%s)"  %  (self.table_name, ",".join(data.keys()), ":".join(data.values()))
        self.database.execute(query)

    def update(self, data: dict):
        query  =   "UPDATE  %s SET %s WHERE id = %s"  %  (self.table_name,  ",".join(data.keys()), id)
        self.database.execute(query)

    def delete(self, id):
        query =   "DELETE FROM  %s WHERE id  =  %s"  %  (self.table_name, id)
        self.database.execute(query)
