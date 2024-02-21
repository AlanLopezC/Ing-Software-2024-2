from flask import Flask

from alchemyClasses import db

from menu import menu
from utils import agregar_tres_entradas


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

if __name__ == '__main__':
    with app.app_context():

        agregar_tres_entradas()
        menu()
