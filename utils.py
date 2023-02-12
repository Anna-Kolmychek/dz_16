import json
import datetime

from config import PATH_TO_DATA
from models import User, Order, Offer


def get_json_form_file(file_name: str) -> dict:
    """получает данные из файла"""
    with open(file_name, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def json_to_models(type_model: str, data_json: dict) -> list[User] | list[Offer] | list[Order]:
    """переводит полученные данные из файлов в формате json
    в список одной из моделей (User, Offer, Order)"""
    data_model = []
    if type_model == "User":
        for line in data_json:
            instance = json_to_user(line)
            data_model.append(instance)
    elif type_model == "Offer":
        for line in data_json:
            instance = json_to_offer(line)
            data_model.append(instance)
    elif type_model == "Order":
        for line in data_json:
            instance = json_to_order(line)
            data_model.append(instance)

    return data_model


def json_to_user(data_json: dict) -> User:
    """переводит данные, полученные из json (по сути на входе словарь) в модель User.
    Функция на перевод ровно одной сущности"""
    instance = User(
        id=data_json['id'],
        first_name=data_json['first_name'],
        last_name=data_json['last_name'],
        age=data_json['age'],
        email=data_json['email'],
        role=data_json['role'],
        phone=data_json['phone'],
    )
    return instance


def json_to_order(data_json: dict) -> Order:
    """переводит данные, полученные из json (по сути на входе словарь) в модель Order.
    Функция на перевод ровно одной сущности"""
    start_date_json = data_json['start_date'].split('/')  # был формат ММ/ДД/ГГГГ
    start_date_sqlite = datetime.date(
        int(start_date_json[2]),
        int(start_date_json[0]),
        int(start_date_json[1])
    )
    end_date_json = data_json['end_date'].split('/')  # был формат ММ/ДД/ГГГГ
    end_date_sqlite = datetime.date(
        int(end_date_json[2]),
        int(end_date_json[0]),
        int(end_date_json[1])
    )
    instance = Order(
        id=data_json['id'],
        name=data_json['name'],
        description=data_json['description'],
        start_date=start_date_sqlite,
        end_date=end_date_sqlite,
        address=data_json['address'],
        price=data_json['price'],
        customer_id=data_json['customer_id'],
        executor_id=data_json['executor_id'],
    )
    return instance


def json_to_offer(data_json: dict) -> Offer:
    """переводит данные, полученные из json (по сути на входе словарь) в модель Offer.
    Функция на перевод ровно одной сущности"""
    instance = Offer(
        id=data_json['id'],
        order_id=data_json['order_id'],
        executor_id=data_json['executor_id'],
    )
    return instance


def get_all_models():
    """загружает данные из всех файлов по PATH и переводит их в соответствующие модели"""
    models = {}
    for type_model, path in PATH_TO_DATA.items():
        data_json = get_json_form_file(path)
        data_model = json_to_models(type_model, data_json)
        models[type_model] = data_model

    return models


def user_to_dict(user: User) -> dict:
    """переводит данные из модели User в словарь.
    Функция на перевод ровно одной сущности"""
    instance = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'age': user.age,
        'email': user.email,
        'role': user.role,
        'phone': user.phone,
    }
    return instance


def lists_user_to_dict(users: list[User]) -> list[dict]:
    """переводит данные из списка моделей User в список словарей.
    Функция на перевод списка сущностей"""
    result = []
    for user in users:
        result.append(user_to_dict(user))
    return result


def order_to_dict(order: Order) -> dict:
    """переводит данные из модели Order в словарь.
    Функция на перевод ровно одной сущности"""
    instance = {
        'id': order.id,
        'name': order.name,
        'description': order.description,
        'start_date': order.start_date,
        'end_date': order.end_date,
        'address': order.address,
        'price': order.price,
        'customer_id': order.customer_id,
        'executor_id': order.executor_id,
    }
    return instance


def lists_order_to_dict(orders: list[Order]) -> list[dict]:
    """переводит данные из списка моделей Order в список словарей.
    Функция на перевод списка сущностей"""
    result = []
    for order in orders:
        result.append(order_to_dict(order))
    return result


def offer_to_dict(offer: Offer) -> dict:
    """переводит данные из модели Offer в словарь.
    Функция на перевод ровно одной сущности"""
    instance = {
        'id': offer.id,
        'order_id': offer.order_id,
        'executor_id': offer.executor_id,
    }
    return instance


def lists_offer_to_dict(offers: list[Offer]) -> list[dict]:
    """переводит данные из списка моделей Order в список словарей.
    Функция на перевод списка сущностей"""
    result = []
    for offer in offers:
        result.append(offer_to_dict(offer))
    return result
