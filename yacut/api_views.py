from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import special_match, get_unique_short_id


@app.route('/api/<int:id>/', methods=['POST'])
def add_short_id(id):
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage('В запросе отсутствуют обязательные поля')
    if 'custom_id' not in data:
        data['custom_id'] = get_unique_short_id()
    short = data['custom_id']
    original = data['url']
    if not original:
        raise InvalidAPIUsage('Обязательные поле не может быть пустым')
    if URLMap.query.filter_by(original=original).first() is not None:
        raise InvalidAPIUsage('Такая ссылка уже есть в базе данных')
    if len(short) > 16:
        raise InvalidAPIUsage('Короткая ссылка не может быть длиннее 16 символов')
    if URLMap.query.filter_by(short=short).first() is not None:
        raise InvalidAPIUsage(f'Имя {short} уже занято!')
    # if short not in SYMBOLS_URL:
    #     raise InvalidAPIUsage('Hедопустимое именя для короткой ссылки')
    short_id = URLMap()
    short_id.from_dict(data)
    db.session.add(short_id)
    db.session.commit()
    return jsonify({'url': short_id.to_dict()['custom_id'],
                    'short_link': short_id.to_dict()['url']}), 201


@app.route('/api/<int:id>/<path:short_id>', methods=['GET'])
def add_original(id, short_id):
    data = request.get_json()
    short_id = data['custom_id']
    url = URLMap.query.filter_by(short=short_id).first_or_404()
       # return jsonify({'message': 'Указанный id не найден'}), 404
    #url = URLMap.query.get_or_404(short_id)
    return jsonify({'url': url.to_dict()['url']}), 200