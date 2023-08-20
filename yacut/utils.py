
import re
import secrets

from settings import MAX_LENGTH, SYMBOLS_URL


def get_unique_short_id():
    short_url_simbols = ''.join(secrets.choice(SYMBOLS_URL) for i in range(MAX_LENGTH))
    return short_url_simbols


def special_match(strg, search=re.compile(r'[^A-z0-9.]').search):
    return bool(search(strg))
