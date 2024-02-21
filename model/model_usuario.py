from alchemyClasses.Usuario import Usuario
from alchemyClasses import db


def inserta_usuario(nombre, apPat, password, email=None, apMat=None, profilePicture=None, superUser=None):
    usuario = Usuario(nombre, apPat, password, email,
                      apMat, profilePicture, superUser)
    db.session.add(usuario)
    db.session.commit()


def filtra_usuario_por_terminacion_apPat(terminacion_apPat):
    return Usuario.query.filter(Usuario.apPat.like(f'%{terminacion_apPat}')).all()


def ver_usuarios():
    return Usuario.query.all()


def filtrar_usuario_por_id(idUsuario):
    return Usuario.query.filter(Usuario.idUsuario == idUsuario).first()


def actualizar_nombre_usuario(idUsuario, nombre):
    usuario = Usuario.query.filter(Usuario.idUsuario == idUsuario).first()

    if usuario:
        usuario.nombre = nombre
        db.session.commit()
        return True
    else:
        return False


def eliminar_usuario_por_id(idUsuario) -> bool:
    usuario = Usuario.query.filter(Usuario.idUsuario == idUsuario).first()

    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    else:
        return False


def eliminar_todos_los_usuarios():
    usuarios = Usuario.query.all()
    for usuario in usuarios:
        db.session.delete(usuario)
    db.session.commit()
    return True
