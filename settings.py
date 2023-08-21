import os
import string

MIN_LENGTH = 1
MAX_LENGTH_GEN = 6
MAX_LENGTH_SHORT = 16
MAX_LENGTH_LONG = 256
SYMBOLS_URL = string.ascii_letters + string.digits


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='fhgdtrew45dgik')
