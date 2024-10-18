import configparser

config = configparser.ConfigParser()
config.read(".env")

class Settings:
    SERVER_HOST: str
    SERVER_PORT: str
    
    DB_PATH: str
    DB_INIT_PATH: str

    DB_HOST: str
    DB_PORT: int
    DB_USERNAME: str
    DB_PASSWORD: str

Settings.SERVER_HOST = config.get('SERVER', 'SERVER_HOST')
Settings.SERVER_PORT = config.get('SERVER', 'SERVER_PORT')

Settings.DB_PATH = config.get('DATABASE', 'DB_PATH')
Settings.DB_INIT_PATH = config.get('DATABASE', 'DB_INIT_PATH')

Settings.DB_HOST = config.get('DATABASE', 'DB_HOST')
Settings.DB_PORT = config.get('DATABASE', 'DB_PORT')
Settings.DB_USERNAME = config.get('DATABASE', 'DB_USERNAME')
Settings.DB_PASSWORD = config.get('DATABASE', 'DB_PASSWORD')
