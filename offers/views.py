from flask import Blueprint, current_app, request

from models import db, Offer
import utils

offers_blueprint = Blueprint('offers_blueprint', __name__)


# Возвращает все записи из Offer
@offers_blueprint.route('/', methods=['GET'])
def get_all_offers():
    with current_app.app_context():
        db_result = db.session.query(Offer).all()

    return utils.lists_offer_to_dict(db_result)


# Возвращает одну запись из Offer по указанному id
@offers_blueprint.route('/<int:offer_id>', methods=['GET'])
def get_single_offer(offer_id):
    with current_app.app_context():
        db_result = db.session.query(Offer).get(offer_id)

    return utils.offer_to_dict(db_result)


# Добавляет новую запись в Offer
@offers_blueprint.route('/', methods=['POST'])
def create_new_offer():
    data_json = request.get_json()
    data_offer = utils.json_to_offer(data_json)
    with current_app.app_context():
        db.session.add(data_offer)
        db.session.commit()
    return 'new offer added'


# Обновляет запись с указанным id на новую в Offer
@offers_blueprint.route('/<int:offer_id>', methods=['PUT'])
def update_offer(offer_id):
    data_json = request.get_json()
    data_offer = utils.json_to_offer(data_json)
    with current_app.app_context():
        offer = db.session.query(Offer).get(offer_id)
        db.session.delete(offer)
        db.session.add(data_offer)
        db.session.commit()
    return f'offer {offer_id} updated'


# Удаляет одну запись из Offer по указанному id
@offers_blueprint.route('/<int:offer_id>', methods=['DELETE'])
def delete_offer(offer_id):
    with current_app.app_context():
        offer = db.session.query(Offer).get(offer_id)
        db.session.delete(offer)
        db.session.commit()
    return f'offer {offer_id} deleted'
