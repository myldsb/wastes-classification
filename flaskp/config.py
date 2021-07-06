'''
the config of the project
'''

import os

class BasicConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    DEBUG = False
    DATABASE_URL = 'mongodb://localhost:27017/'
    DATABASE = 'garbage'
    ADMIN_GROUP = 'admin'
    GUEST_GROUP = 'guest'


class ProductionConfig(BasicConfig):
    pass

class DevelopmentConfig(BasicConfig):
    DEBUG = True

class TestConfig(BasicConfig):
    pass


config = {
    'ProductionConfig': ProductionConfig,
    'DevelopmentConfig': DevelopmentConfig,
    'TestConfig':TestConfig,
    'Default': DevelopmentConfig
}

condig_obj = os.environ.get('FLASK_ENV') or config['Default']