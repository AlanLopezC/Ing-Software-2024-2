
from flask import Blueprint, request, render_template, flash, url_for
from random import randint

from alchemyClasses.Usuario import Usuario
from alchemyClasses import db
from alchemyClasses.Renta import Renta

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuarios')

# Menu
# 1. Ver todos los usuarios
# 2. Ver usuario por id
# 3. Agregar usuario
# 4. Editar usuario
# 5. Eliminar usuario


@usuario_blueprint.route('/menu')
def menu_usuario():
    return render_template('usuario/menu_usuario.html')


@usuario_blueprint.route('/')  # localhost:5000/usuarios/
def ver_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario/ver_usuarios.html', usuarios=usuarios)


# responde a localhost:5000/usuario/id/1


# <tipo:nombre_variable>
@usuario_blueprint.route('/id/<int:id_usuario>')
def ver_usuario_id(id_usuario):
    usuario = Usuario.query.filter(Usuario.idUsuario == id_usuario).first()
    if usuario is None:
        return "No existe el usuario"
    return render_template('usuario/ver_usuario.html', usuario=usuario)

# Form para solicitar el id del usuario a ver
# responde a localhost:5000/usuario/ver


@usuario_blueprint.route('/id')
def ver_usuario():
    if request.method == 'GET':
        return render_template('usuario/ver.html')
    else:
        id_usuario = request.form['id_usuario']
        # checar que id sea numero
        if not id_usuario.isdigit():
            return "El id debe ser un número"
        url_for('usuario.ver_usuario', id_usuario=id_usuario)
        return render_template('usuario/ver_usuario.html', id_usuario=id_usuario)


@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('usuario/agregar_usuario.html')
    else:
        # Obtengo la información del método post.
        nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        password = request.form['password']
        email = request.form['email']
        # profile_picture = request.form['profilePicture']
        # super_user = request.form['superUser']

        # Creo mi usuario.
        usuario = Usuario(nombre, ap_pat, password, email,
                          ap_mat)
        # Lo guardo en la DB
        db.session.add(usuario)
        db.session.commit()
        # url_for
        # flash
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('usuario.agregar_usuario')
        # Y regreso al flujo que me hayan especificado.
        return render_template('usuario/usuario_agregado.html', nombre=nombre, email=email)


@usuario_blueprint.route('/editar', methods=['GET', 'POST'])
def editar_usuario():
    if request.method == 'GET':
        return render_template('usuario/editar_usuario.html')
    else:
        id_usuario = request.form['id_usuario']

        usuario = Usuario.query.filter(Usuario.idUsuario == id_usuario).first()
        if usuario is None:
            return "No existe el usuario"

        nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        password = request.form['password']
        email = request.form['email']

        if nombre:
            usuario.nombre = nombre
        if ap_pat:
            usuario.apPat = ap_pat
        if ap_mat:
            usuario.apMat = ap_mat
        if password:
            usuario.password = password
        if email:
            usuario.email = email

        db.session.commit()

        return render_template('usuario/editar_usuario.html', usuario=usuario)


@usuario_blueprint.route('/eliminar', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'GET':
        return render_template('usuario/eliminar_usuario.html')
    else:
        id_usuario = request.form['id_usuario']
        usuario = Usuario.query.filter(Usuario.idUsuario == id_usuario).first()
        if usuario is None:
            return "No existe el usuario"

        # Debemos checar si el usuario tiene dependencias (renta)
        # Si tiene dependencias no se puede eliminar
        renta = Renta.query.filter(
            Renta.idUsuario == usuario.idUsuario).first()
        if renta is not None:
            return f"El usuario {usuario.nombre} tiene rentas asociadas, no se puede eliminar"

        db.session.delete(usuario)
        db.session.commit()
        return f"ID: {usuario.idUsuario}, Usuario {usuario.nombre} eliminado"
