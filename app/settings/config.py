import configparser
import os


config = configparser.ConfigParser()
config.read(".env")


class Settings:
    SERVER_HOST: str
    SERVER_PORT: int
    DB_PATH: str
    DB_INIT_PATH: str

    # Попытка загрузить значения из .env или переменных окружения
    SERVER_HOST = config.get(
        "SERVER",
        "SERVER_HOST",
        fallback=os.getenv("SERVER_HOST", "127.0.0.1"),
    )
    SERVER_PORT = int(
        config.get("SERVER", "SERVER_PORT", fallback=os.getenv("SERVER_PORT", "8000")),
    )
    DB_PATH = config.get(
        "DATABASE",
        "DB_PATH",
        fallback=os.getenv("DB_SQLITE_PATH", "/database/db.db"),
    )
    DB_INIT_PATH = config.get(
        "DATABASE",
        "DB_INIT_PATH",
        fallback=os.getenv("DB_SQLITE_INIT", "/database/init.sql"),
    )
