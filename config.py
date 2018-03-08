class Config(object):
    """
    Configurations base class
    """
    POSTS_PER_PAGE = 5
    MONGO_URI = "mongodb://justinliu:246813579@ds259768.mlab.com:59768/enerknol"
    ELASTIC_HOST = ['https://jsy0vkfpyo:nu4ueefwd7@holly-2620832.us-east-1.bonsaisearch.net']

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
