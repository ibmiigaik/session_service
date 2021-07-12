import configparser
import pathlib

config_path = pathlib.Path(__file__).parent.resolve() / "config.ini"
config_ini = configparser.ConfigParser()
config_ini.read(config_path)


def empty_str_cast(value, default=None):
    if not value:
        return default

    return value

def gen_secret_key():
    return 'super secret key'


class ServerConfig:
    SECRET_KEY = empty_str_cast(config_ini["server"]["SECRET_KEY"]) or gen_secret_key()


class DevelopmentConfig(ServerConfig):
    #APPLICATION_ROOT = '/auth'

    SECRET_KEY = "development secret key"
    DEBUG = True

    MONGODB_HOST = 'mongomock://localhost'
    MONGODB_DB = 'testing1'

    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = config_ini['server']['SESSION_FILE_DIR']


Config = DevelopmentConfig()
