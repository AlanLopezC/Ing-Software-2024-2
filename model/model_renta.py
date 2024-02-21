import datetime
from alchemyClasses.Renta import Renta
from alchemyClasses import db


def inserta_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
    renta = Renta(idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus)
    db.session.add(renta)
    db.session.commit()


def eliminar_rentas_anteriores_a_tres_dias():
    rentas = Renta.query.filter(Renta.fecha_renta < (
        datetime.datetime.now() - datetime.timedelta(days=3))).all()
    for renta in rentas:
        db.session.delete(renta)
    db.session.commit()
    return rentas


def ver_rentas():
    return Renta.query.all()


def filtrar_renta_por_id(idRenta):
    return Renta.query.filter(Renta.idRentar == idRenta).first()


def actualizar_fecha_renta(idRenta, fecha_renta: datetime.datetime):
    renta = Renta.query.filter(Renta.idRentar == idRenta).first()

    if renta:
        renta.fecha_renta = fecha_renta
        db.session.commit()
        return True
    else:
        return False


def eliminar_renta_por_id(idRenta) -> bool:
    renta = Renta.query.filter(Renta.idRentar == idRenta).first()

    if renta:
        db.session.delete(renta)
        db.session.commit()
        return True
    else:
        return False


def eliminar_todas_las_rentas():
    rentas = Renta.query.all()
    for renta in rentas:
        db.session.delete(renta)
    db.session.commit()
    return True
