from distutils.log import DEBUG

# we assign values to configuration variables that will be used by the app Eg ApiKey
class Config:  
    NEWS_BASE_URL_SOURCES = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_BASE_EVERYTHING_URL = 'https://newsapi.org/v2/everything?domains={}&apiKey={}'
    NEWS_BASE_HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    NEWS_BASE_SOURCE = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

    API_KEY = "37a78df4920142b683f679fffd728ab9"
    SECRET_KEY ="renahwambura"
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options= {
    'development': DevConfig,
    'production': ProdConfig
}