from flask import Flask
from sqlalchemy import and_, or_

from alchemyClasses import db
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256


# mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
# <dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
# mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        # for alumno in Alumno.query.all():  # Select * from alumno
        #     print(alumno)
        pass
        # Create
        # valeria = Alumno('Valeria', 'Ramirez', 319311918, apMat=None,
        #                  password=sha256(cipher("Developer123!")).hexdigest())
        # db.session.add(valeria)
        # db.session.commit()
        # Update
        # Primero tenemos que buscar el objeto que queremos.
        # Ya que lo tengo, entonces cambio el atributo.
        # Y entonces hago el commit.
        # fer = Alumno.query.filter(Alumno.nombre == 'Fernando').first()
        # print(type(fer))
        # fer.nombre = "Fer"
        # fer.ap_mat = "Baeza"
        # db.session.commit()
        # Delete
        # borra_alumno(313320679)
        # print("Borrado con éxito!")
