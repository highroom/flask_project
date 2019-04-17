class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'asdfsdf'


class DevConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True