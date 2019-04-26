import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mwai@localhost/moha'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'  #enables  a transport layer securty to secure emails
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")



    # @staticmethod
    # def init_app(app):
    #     pass


class ProdConfig(Config):
    pass
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



# class TestConfig(Config):
#     # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://thomas:psqltoto29@localhost/pitchperfect_test'
#     pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kiki@localhost/pitch'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
