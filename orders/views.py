from flask import Blueprint, current_app, request

from models import db, Order
import utils

orders_blueprint = Blueprint('orders_blueprint', __name__)


# Возвращает все записи из Order
@orders_blueprint.route('/', methods=['GET'])
def get_all_orders():
    with current_app.app_context():
        db_result = db.session.query(Order).all()

    return utils.lists_order_to_dict(db_result)


# Возвращает одну запись из Order по указанному id
@orders_blueprint.route('/<int:order_id>', methods=['GET'])
def get_single_order(order_id):
    with current_app.app_context():
        db_result = db.session.query(Order).get(order_id)

    return utils.order_to_dict(db_result)


# Добавляет новую запись в Order
@orders_blueprint.route('/', methods=['POST'])
def create_new_order():
    data_json = request.get_json()
    data_order = utils.json_to_order(data_json)
    with current_app.app_context():
        db.session.add(data_order)
        db.session.commit()
    return 'new order added'


# Обновляет запись с указанным id на новую в Order
@orders_blueprint.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    data_json = request.get_json()
    data_order = utils.json_to_order(data_json)
    with current_app.app_context():
        order = db.session.query(Order).get(order_id)
        db.session.delete(order)
        db.session.add(data_order)
        db.session.commit()
    return f'order {order_id} updated'


# Удаляет одну запись из Order по указанному id
@orders_blueprint.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    with current_app.app_context():
        order = db.session.query(Order).get(order_id)
        db.session.delete(order)
        db.session.commit()
    return f'order {order_id} deleted'
