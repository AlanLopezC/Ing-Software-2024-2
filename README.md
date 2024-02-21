# P1. Introducción a Python

## Entorno Virtual

En Windows, ejecuta:

```
super-env\Scripts\activate
pip install -r requirements.txt
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
source super-env/bin/activate
pip install -r requirements.txt
```

(Este script está escrito para la consola bash. Si usas las consolas csh or fish, hay scripts alternativos activate.csh y activate.fish que deberá usar en su lugar.)

Para desactivar el entorno virtual, digita:

```
deactivate
```

## Script 1

- Simulación de un juego de tennis.

Primero iniciar entorno virtual.

Después:

```
python Script1.py
```

## Script 2

- Función de caminata, en la que se recibe una cadena de un camino (UDUD (2 montañas)) y se regresa el número de montañas y de valles.

- Implementación de un BST (árbol binario ordenado). Con la función insert, inorder, preorder y postorder.

### **Importante**

Para que funcionen las pruebas hay que descomentar en el final archivo las llamadas de las funciones de la prueba que se desee realizar.

Primero iniciar entorno virtual.

Después:

```
python Script2.py
```

## Script 3

- Graficación de una función lineal usando matplotlib.

Primero iniciar entorno virtual.

Después:

```
python Script3.py
```
