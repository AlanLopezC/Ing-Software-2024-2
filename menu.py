from model.model_usuario import *
from model.model_pelicula import *
from model.model_renta import *


def menu():
    print("Menú con 5 opciones:")
    print("1. Ver los registros de una tabla.")
    print("2. Filtrar los registros de una tabla por id.")
    print("3. Actualizar la columna nombre de un registro, para el caso de la tabla Renta, modificar la fecha de la renta.")
    print("4. Eliminar un registro por id")
    print("5. Eliminar todos los registros de una tabla.")

    opcion = -1
    while opcion < 1 or opcion > 5:
        try:
            opcion = int(input("Elige una opción: "))
            if opcion < 1 or opcion > 5:
                print("Elige una opción válida.")
        except ValueError:
            print("Elige una opción válida.")

    print("")
    # 1. Ver los registros de una tabla.
    if opcion == 1:
        print("1. Usuarios")
        print("2. Peliculas")
        print("3. Rentas")
        tabla = -1
        while tabla < 1 or tabla > 3:
            try:
                tabla = int(input("Elige una tabla: "))
                if tabla < 1 or tabla > 3:
                    print("Elige una opción válida.")
            except ValueError:
                print("Elige una opción válida.")

        print("")
        if tabla == 1:
            usuarios = ver_usuarios()
            if len(usuarios) == 0:
                print("No hay usuarios.")
            else:
                for usuario in usuarios:
                    print(usuario)

        elif tabla == 2:
            peliculas = ver_peliculas()
            if len(peliculas) == 0:
                print("No hay películas.")
            else:
                for pelicula in peliculas:
                    print(pelicula)

        elif tabla == 3:
            rentas = ver_rentas()
            if len(rentas) == 0:
                print("No hay rentas.")
            else:
                for renta in rentas:
                    print(renta)

    # 2. Filtrar los registros de una tabla por id.
    elif opcion == 2:
        print("1. Usuarios")
        print("2. Peliculas")
        print("3. Rentas")
        tabla = -1
        while tabla < 1 or tabla > 3:
            try:
                tabla = int(input("Elige una tabla: "))
                if tabla < 1 or tabla > 3:
                    print("Elige una opción válida.")
            except ValueError:
                print("Elige una opción válida.")

        print("")
        if tabla == 1:
            idUsuario = -1
            while idUsuario < 0:
                try:
                    idUsuario = int(input("Escribe el id del usuario: "))
                except ValueError:
                    print("Escribe un id válido.")

            usuario = filtrar_usuario_por_id(idUsuario)
            print(usuario)

        elif tabla == 2:
            idPelicula = -1
            while idPelicula < 0:
                try:
                    idPelicula = int(
                        input("Escribe el id de la película: "))
                except ValueError:
                    print("Escribe un id válido.")
            pelicula = filtrar_pelicula_por_id(idPelicula)
            print(pelicula)

        elif tabla == 3:
            idRenta = -1
            while idRenta < 0:
                try:
                    idRenta = int(input("Escribe el id de la renta: "))
                except ValueError:
                    print("Escribe un id válido.")
            renta = filtrar_renta_por_id(idRenta)
            print(renta)

    # 3. Actualizar la columna nombre de un registro, para el caso de la tabla Renta, modificar la fecha de la renta.
    elif opcion == 3:
        print("1. Usuarios")
        print("2. Peliculas")
        print("3. Rentas")
        tabla = -1
        while tabla < 1 or tabla > 3:
            try:
                tabla = int(input("Elige una tabla: "))
                if tabla < 1 or tabla > 3:
                    print("Elige una opción válida.")
            except ValueError:
                print("Elige una opción válida.")

        print("")
        if tabla == 1:
            idUsuario = -1
            while idUsuario < 0:
                try:
                    idUsuario = int(input("Escribe el id del usuario: "))
                except ValueError:
                    print("Escribe un id válido.")

            nombre = input("Escribe el nuevo nombre: ")
            exitoso = actualizar_nombre_usuario(idUsuario, nombre)
            if exitoso:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

        elif tabla == 2:
            idPelicula = -1
            while idPelicula < 0:
                try:
                    idPelicula = int(
                        input("Escribe el id de la película: "))
                except ValueError:
                    print("Escribe un id válido.")

            nombre = input("Escribe el nuevo nombre: ")
            exitoso = actualizar_nombre_pelicula(idPelicula, nombre)
            if exitoso:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

        elif tabla == 3:
            idRenta = -1
            while idRenta < 0:
                try:
                    idRenta = int(input("Escribe el id de la renta: "))
                except ValueError:
                    print("Escribe un id válido.")

            while True:
                try:
                    fecha_renta = input(
                        "Escribe la nueva fecha de renta (yyyy-mm-dd): ")
                    fecha_datetime = datetime.datetime.strptime(
                        fecha_renta, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Escribe una fecha válida.")

            exitoso = actualizar_fecha_renta(idRenta, fecha_datetime)
            if exitoso:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

    # 4. Eliminar un registro por id
    elif opcion == 4:
        print("1. Usuarios")
        print("2. Peliculas")
        print("3. Rentas")
        tabla = -1
        while tabla < 1 or tabla > 3:
            try:
                tabla = int(input("Elige una tabla: "))
                if tabla < 1 or tabla > 3:
                    print("Elige una opción válida.")
            except ValueError:
                print("Elige una opción válida.")

        print("")
        if tabla == 1:
            idUsuario = -1
            while idUsuario < 0:
                try:
                    idUsuario = int(input("Escribe el id del usuario: "))
                except ValueError:
                    print("Escribe un id válido.")

            eliminado = eliminar_usuario_por_id(idUsuario)
            if eliminado:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

        elif tabla == 2:
            idPelicula = -1
            while idPelicula < 0:
                try:
                    idPelicula = int(
                        input("Escribe el id de la película: "))
                except ValueError:
                    print("Escribe un id válido.")

            eliminado = eliminar_pelicula_por_id(idPelicula)
            if eliminado:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

        elif tabla == 3:
            idRenta = -1
            while idRenta < 0:
                try:
                    idRenta = int(input("Escribe el id de la renta: "))
                except ValueError:
                    print("Escribe un id válido.")

            eliminado = eliminar_renta_por_id(idRenta)
            if eliminado:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

    # 5. Eliminar todos los registros de una tabla.
    elif opcion == 5:
        print("1. Usuarios")
        print("2. Peliculas")
        print("3. Rentas")
        tabla = -1
        while tabla < 1 or tabla > 3:
            try:
                tabla = int(input("Elige una tabla: "))
                if tabla < 1 or tabla > 3:
                    print("Elige una opción válida.")
            except ValueError:
                print("Elige una opción válida.")

        print("")
        if tabla == 1:
            eliminado = eliminar_todos_los_usuarios()
            if eliminado:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

        elif tabla == 2:
            eliminado = eliminar_todas_las_peliculas()
            if eliminado:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")

        elif tabla == 3:
            eliminado = eliminar_todas_las_rentas()
            if eliminado:
                print("Operación exitosa.")
            else:
                print("No se encontró el id.")
