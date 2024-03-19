
from flask import Blueprint, request, render_template, flash, url_for
from random import randint

from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db
from alchemyClasses.Renta import Renta
from alchemyClasses.Usuario import Usuario
from datetime import date
import datetime as dt

renta_blueprint = Blueprint('renta', __name__, url_prefix='/rentas')


@renta_blueprint.route('/menu')
def menu_renta():
    return render_template('renta/menu_renta.html')


@renta_blueprint.route('/')  # localhost:5000/rentas/
def ver_rentas():
    rentas = Renta.query.all()
    return render_template('renta/ver_rentas.html', rentas=rentas, datetime=dt)


# responde a localhost:5000/renta/id/1


# <tipo:nombre_variable>
@renta_blueprint.route('/id/<int:id_renta>')
def ver_renta_id(id_renta):
    renta = Renta.query.filter(
        Renta.idRentar == id_renta).first()
    if renta is None:
        return "No existe el renta"
    return render_template('renta/ver_renta.html', renta=renta)

# Form para solicitar el id del renta a ver
# responde a localhost:5000/renta/ver


@renta_blueprint.route('/id')
def ver_renta():
    if request.method == 'GET':
        return render_template('renta/ver.html')
    else:
        id_renta = request.form['id_renta']
        # checar que id sea numero
        if not id_renta.isdigit():
            return "El id debe ser un número"
        url_for('renta.ver_renta', id_renta=id_renta)
        return render_template('renta/ver_renta.html', id_renta=id_renta)


@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('renta/agregar_renta.html')
    else:
        # Obtengo la información del método post.
        id_usuario = request.form['id_usuario']
        id_pelicula = request.form['id_pelicula']

        # checar si ids son numericos y existen
        if not id_usuario.isdigit():
            return "El id de usuario debe ser un número"
        if not id_pelicula.isdigit():
            return "El id de pelicula debe ser un número"

        usuario = Usuario.query.filter(Usuario.idUsuario == id_usuario).first()
        if usuario is None:
            return "No existe el usuario"

        pelicula = Renta.query.filter(
            Pelicula.idPelicula == id_pelicula).first()
        if pelicula is None:
            return "No existe la pelicula"

        # Creo mi renta. con fecha de hoy y duracion 5 dias
        renta = Renta(id_usuario, id_pelicula, date.today(), 5)
        # Lo guardo en la DB
        db.session.add(renta)
        db.session.commit()
        # url_for
        # flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('renta.agregar_renta')
        # Y regreso al flujo que me hayan especificado.
        return render_template('renta/renta_agregado.html', id_pelicula=id_pelicula, id_usuario=id_usuario, fecha=date.today(), duracion=5)


@renta_blueprint.route('/editar', methods=['GET', 'POST'])
def editar_renta():
    if request.method == 'GET':
        return render_template('renta/editar_renta.html')
    else:
        id_renta = request.form['id_renta']

        renta = Renta.query.filter(
            Renta.idRentar == id_renta).first()
        if renta is None:
            return "No existe el renta"

        estatus = request.form['estatus']

        if estatus:
            # Estatus solo puede ser 0 o 1
            if estatus != '0' and estatus != '1':
                return "Estatus debe ser 0 (no entregado) o 1 (entregado)"
            renta.estatus = estatus
            db.session.commit()

        return render_template('renta/editar_renta.html', renta=renta)
