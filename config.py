import os.path

# Константы
PATH_TO_DATA = {
    'Offer': os.path.join('data', 'offers.json'),
    'Order': os.path.join('data', 'orders.json'),
    'User': os.path.join('data', 'users.json'),
}


# Настройки для приложения
class Config:
    # SQLALCHEMY_DATABASE_URI = "sqlite:///sqlite3.db"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False