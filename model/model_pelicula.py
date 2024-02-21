from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db


def inserta_pelicula(nombre, genero, duracion, inventario):
    pelicula = Pelicula(nombre, genero, duracion, inventario)
    db.session.add(pelicula)
    db.session.commit()


def cambiar_genero_pelicula(nombre, genero):
    pelicula = Pelicula.query.filter(Pelicula.nombre == nombre).first()
    pelicula.genero = genero
    db.session.commit()


def ver_peliculas():
    return Pelicula.query.all()


def filtrar_pelicula_por_id(idPelicula):
    return Pelicula.query.filter(Pelicula.idPelicula == idPelicula).first()


def actualizar_nombre_pelicula(idPelicula, nombre) -> bool:
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == idPelicula).first()

    if pelicula:
        pelicula.nombre = nombre
        db.session.commit()
        return True
    else:
        return False


def eliminar_pelicula_por_id(idPelicula):
    pelicula = Pelicula.query.filter(Pelicula.idPelicula == idPelicula).first()

    if pelicula:
        db.session.delete(pelicula)
        db.session.commit()
        return True
    else:
        return False
