import re
import secrets

from settings import MAX_LENGTH_GEN, SYMBOLS_URL
from .models import URLMap


def get_unique_short_id():
    short_id = ''.join(secrets.choice(SYMBOLS_URL) for _ in range(MAX_LENGTH_GEN))
    if not URLMap.query.filter_by(short=short_id).first():
        return short_id


def special_match(strg, search=re.compile(r'[^A-z0-9.]').search):
    return bool(search(strg))
