class Config(object):
    """
    Configurations base class
    """
    POSTS_PER_PAGE = 5
    MONGO_URI = "mongodb://localhost:27017"
    ELASTIC_HOST = [{ "host" : "localhost", "port" : 9200 }]

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
