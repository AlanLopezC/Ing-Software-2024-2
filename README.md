# P1. Introducción a Python

## Entorno Virtual

En Windows, ejecuta:

```
venv\Scripts\activate
```

- Ojo: por default windows no deja correr scripts, así está en default:

```
 Set-ExecutionPolicy Restricted
```

Es necesario correr en Powershell en Administrador el siguiente comando:

```
Set-ExecutionPolicy RemoteSigned
```

En Unix o MacOS, ejecuta:

```
source venv/bin/activate
```

(Este script está escrito para la consola bash. Si usas las consolas csh or fish, hay scripts alternativos activate.csh y activate.fish que deberá usar en su lugar.)

Para desactivar el entorno virtual, digita:

```
deactivate
```

## Correr el programa

Primero se debe activar el entorno.

Segundo, se debe activar la base de datos en mysql workbench con puerto localhost:3306 y correr el archivo IngSoftLab.sql para crear la base de datos.

Después:

```
python app.py
```

Cada vez que se ejecuta se agregará denuevo un usuario, pelicula y renta. Para evitar esto, se debe comentar la linea 19 (funcion agregar_tres_entradas).
