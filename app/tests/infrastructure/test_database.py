from infrastructure.database.sqlite import SQLiteDatabase, sqlite_database_build


def create_database_connection():
    sqllite_client: SQLiteDatabase = sqlite_database_build()
    
    assert sqllite_client.is_open == True