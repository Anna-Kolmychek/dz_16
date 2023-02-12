from flask import Flask

import utils
from config import Config
from models import db
from users.views import users_blueprint
from offers.views import offers_blueprint
from orders.views import orders_blueprint

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Создаем БД, получаем данные из файлов json, заносим полученные данные в БД
with app.app_context():
    db.create_all()
    models = utils.get_all_models()
    db.session.add_all(models['User'])
    db.session.add_all(models['Offer'])
    db.session.add_all(models['Order'])
    db.session.commit()


# Подключаем блюпринты
app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(offers_blueprint, url_prefix='/offers')
app.register_blueprint(orders_blueprint, url_prefix='/orders')


if __name__ == "__main__":
    app.run()
