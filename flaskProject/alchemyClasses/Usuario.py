from sqlalchemy import Column, Integer, String

from alchemyClasses import db


class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    apPat = Column(String(200))
    apMat = Column(String(200), nullable=True)
    password = Column(String(64))
    email = Column(String(500), unique=True, nullable=True)
    profilePicture = Column(db.LargeBinary)
    superUser = Column(Integer, nullable=True)

    def __init__(self, nombre, apPat, password, email=None, apMat=None, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profilePicture
        self.superUser = superUser

    def __str__(self):
        return f'Nombre:{self.nombre}\nEmail:{self.email}'