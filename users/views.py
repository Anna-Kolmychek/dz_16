from flask import Blueprint, current_app, request

from models import db, User
import utils

users_blueprint = Blueprint('users_blueprint', __name__)


# Возвращает все записи из User
@users_blueprint.route('/', methods=['GET'])
def get_all_users():
    with current_app.app_context():
        db_result = db.session.query(User).all()

    return utils.lists_user_to_dict(db_result)


# Возвращает одну запись из User по указанному id
@users_blueprint.route('/<int:uid>', methods=['GET'])
def get_single_user(uid):
    with current_app.app_context():
        db_result = db.session.query(User).get(uid)

    return utils.user_to_dict(db_result)


# Добавляет новую запись в User
@users_blueprint.route('/', methods=['POST'])
def create_new_user():
    data_json = request.get_json()
    data_user = utils.json_to_user(data_json)
    with current_app.app_context():
        db.session.add(data_user)
        db.session.commit()
    return 'new user added'


# Обновляет запись с указанным id на новую в User
@users_blueprint.route('/<int:uid>', methods=['PUT'])
def update_user(uid):
    data_json = request.get_json()
    data_user = utils.json_to_user(data_json)
    with current_app.app_context():
        user = db.session.query(User).get(uid)
        db.session.delete(user)
        db.session.add(data_user)
        db.session.commit()
    return f'user {uid} updated'


# Удаляет одну запись из User по указанному id
@users_blueprint.route('/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    with current_app.app_context():
        user = db.session.query(User).get(uid)
        db.session.delete(user)
        db.session.commit()
    return f'user {uid} deleted'
