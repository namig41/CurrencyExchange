import configparser

config = configparser.ConfigParser()
config.read(".env")

class Settings:
    DB_PATH: str
    INIT_PATH: str

    HOST: str
    PORT: int
    USERNAME: str
    PASSWORD: str



Settings.DB_PATH = config.get('Database', 'DB_PATH')
Settings.INIT_PATH = config.get('Database', 'INIT_PATH')
Settings.HOST = config.get('Database', 'HOST')
Settings.PORT = config.get('Database', 'PORT')
Settings.USERNAME = config.get('Database', 'USERNAME')
Settings.PASSWORD = config.get('Database', 'PASSWORD')
