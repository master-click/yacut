import re

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    urlmap = URLMap.query.filter_by(short=short_id).first()
    if urlmap is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': urlmap.original}), 200


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if 'custom_id' in data:
        if not data['custom_id']:
            data['custom_id'] = get_unique_short_id()
        elif not re.match(r'^[a-zA-Z0-9]{1,16}$', data['custom_id']):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')
        elif URLMap.query.filter_by(short=data['custom_id']).first() is not None:
            raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.')
    else:
        data['custom_id'] = get_unique_short_id()
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    short_url = url_for('link_view', short=urlmap.short, _external=True)
    return jsonify({'url': urlmap.original, 'short_link': short_url}), 201
