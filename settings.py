import os
import string

MAX_LENGTH = 6
MAX_CUSTOM_LENGTH = 16
SYMBOLS_URL = string.ascii_letters + string.digits


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='fhgdtrew45dgik')
