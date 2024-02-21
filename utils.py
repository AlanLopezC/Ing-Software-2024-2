
import datetime
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses import db


from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256


def agregar_tres_entradas():
    usuario = Usuario('Ferni', 'Lopez', sha256(
        cipher("Developer123!")).hexdigest())

    pelicula = Pelicula('El Padrino', 'Suspenso', 200)

    renta = Renta(1, 1, datetime.datetime.now())

    db.session.add(usuario)
    db.session.commit()
    db.session.add(pelicula)
    db.session.commit()
    db.session.add(renta)
    db.session.commit()
