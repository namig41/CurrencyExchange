from infrastructure.database.sqlite import (
    sqlite_database_factory,
    SQLiteDatabase,
)


def create_database_connection():
    sqlite_client: SQLiteDatabase = sqlite_database_factory()

    assert sqlite_client.is_open
