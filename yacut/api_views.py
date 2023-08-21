from http import HTTPStatus

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import special_match, get_unique_short_id
from settings import MAX_CUSTOM_LENGTH


@app.route('/api/id/', methods=['POST'])
def add_short_id():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    if data.get('custom_id') is None or len(data.get('custom_id')) == 0:
        data['custom_id'] = get_unique_short_id()
    original = data['url']
    short = data['custom_id']
    if original is None:
        raise InvalidAPIUsage('Обязательные поле не может быть пустым')
    if len(short) > MAX_CUSTOM_LENGTH or special_match(short):
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
    if URLMap.query.filter_by(short=short).first():
        raise InvalidAPIUsage(f'Имя "{short}" уже занято.')
    short_id = URLMap(original=original, short=short)
    short_id.from_dict(data)
    db.session.add(short_id)
    db.session.commit()
    return jsonify(short_id.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def add_original(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    if not url:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({"url": url.original})