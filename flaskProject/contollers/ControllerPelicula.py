
from flask import Blueprint, request, render_template, flash, url_for
from random import randint

from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db
from alchemyClasses.Renta import Renta

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/peliculas')


@pelicula_blueprint.route('/menu')
def menu_pelicula():
    return render_template('pelicula/menu_pelicula.html')


@pelicula_blueprint.route('/')  # localhost:5000/peliculas/
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('pelicula/ver_peliculas.html', peliculas=peliculas)


# responde a localhost:5000/pelicula/id/1


# <tipo:nombre_variable>
@pelicula_blueprint.route('/id/<int:id_pelicula>')
def ver_pelicula_id(id_pelicula):
    pelicula = Pelicula.query.filter(
        Pelicula.idPelicula == id_pelicula).first()
    if pelicula is None:
        return "No existe el pelicula"
    return render_template('pelicula/ver_pelicula.html', pelicula=pelicula)

# Form para solicitar el id del pelicula a ver
# responde a localhost:5000/pelicula/ver


@pelicula_blueprint.route('/id')
def ver_pelicula():
    if request.method == 'GET':
        return render_template('pelicula/ver.html')
    else:
        id_pelicula = request.form['id_pelicula']
        # checar que id sea numero
        if not id_pelicula.isdigit():
            return "El id debe ser un número"
        url_for('pelicula.ver_pelicula', id_pelicula=id_pelicula)
        return render_template('pelicula/ver_pelicula.html', id_pelicula=id_pelicula)


@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('pelicula/agregar_pelicula.html')
    else:
        # Obtengo la información del método post.
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']

        # checar si duracion e inventario son numeros
        if not duracion.isdigit():
            return "La duración debe ser un número"
        if not inventario.isdigit():
            return "El inventario debe ser un número"

        # Creo mi pelicula.
        pelicula = Pelicula(nombre, genero, duracion, inventario)
        # Lo guardo en la DB
        db.session.add(pelicula)
        db.session.commit()
        # url_for
        # flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('pelicula.agregar_pelicula')
        # Y regreso al flujo que me hayan especificado.
        return render_template('pelicula/pelicula_agregado.html', nombre=nombre, genero=genero)


@pelicula_blueprint.route('/editar', methods=['GET', 'POST'])
def editar_pelicula():
    if request.method == 'GET':
        return render_template('pelicula/editar_pelicula.html')
    else:
        id_pelicula = request.form['id_pelicula']

        pelicula = Pelicula.query.filter(
            Pelicula.idPelicula == id_pelicula).first()
        if pelicula is None:
            return "No existe el pelicula"

        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']

        if nombre:
            pelicula.nombre = nombre
        if genero:
            pelicula.genero = genero
        if duracion:
            if not duracion.isdigit():
                return "La duración debe ser un número"
            pelicula.duracion = duracion
        if inventario:
            if not inventario.isdigit():
                return "El inventario debe ser un número"
            pelicula.inventario = inventario

        db.session.commit()

        return render_template('pelicula/editar_pelicula.html', pelicula=pelicula)


@pelicula_blueprint.route('/eliminar', methods=['GET', 'POST'])
def eliminar_pelicula():
    if request.method == 'GET':
        return render_template('pelicula/eliminar_pelicula.html')
    else:
        id_pelicula = request.form['id_pelicula']
        pelicula = Pelicula.query.filter(
            Pelicula.idPelicula == id_pelicula).first()
        if pelicula is None:
            return "No existe el pelicula"

        # Debemos checar si el pelicula tiene dependencias (renta)
        # Si tiene dependencias no se puede eliminar
        renta = Renta.query.filter(
            Renta.idPelicula == pelicula.idPelicula).first()
        if renta is not None:
            return f"El pelicula {pelicula.nombre} tiene rentas asociadas, no se puede eliminar"

        db.session.delete(pelicula)
        db.session.commit()
        return f"ID: {pelicula.idPelicula}, Pelicula {pelicula.nombre} eliminado"
