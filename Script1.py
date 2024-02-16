import random


SAQUE = random.choice([1, 2])


def cambio_cancha():
    print("Cambio de cancha!!")


def cambio_saque():
    global SAQUE

    print("-----------------------")
    if SAQUE == 1:
        print("Cambio de saque")
        print("Saca el jugador 2")
        SAQUE = 2
    else:
        print("Cambio de saque")
        print("Saca el jugador 1")
        SAQUE = 1
    print("-----------------------")


def punto():
    return random.choice([0, 1])


def convertir_puntos(p1, p2):
    """
    p1: puntos a convertir
    p2: puntos de contrincante
    """
    if p1 == 0:
        return "0"
    if p1 == 1:
        return "15"
    if p1 == 2:
        return "30"
    if p1 == 3:
        return "40"

    if p1 - p2 >= 2:
        return "Ganado"
    if p1 - p2 == 1:
        return "AD"
    if p1 == p2 or p1 - p2 == -1:
        return "40"


def juego():
    p1 = 0
    p2 = 0
    while True:
        print(
            f"Puntos: {convertir_puntos(p1, p2)} - {convertir_puntos(p2, p1)}")
        if p1 >= 4 and p1 - p2 >= 2:
            return 1
        if p2 >= 4 and p2 - p1 >= 2:
            return 2

        if punto() == 0:
            print("Punto para el jugador 1")
            p1 += 1
        else:
            print("Punto para el jugador 2")
            p2 += 1


def set():
    p1 = 0
    p2 = 0
    while True:
        print(f"Juegos: {p1} - {p2}")

        if (p1 + p2) % 2 == 1:
            cambio_cancha()

        if p1 >= 6 and p1 - p2 >= 2:
            return 1
        if p2 >= 6 and p2 - p1 >= 2:
            return 2

        if juego() == 1:
            print("Gana el juego el jugador 1")
            p1 += 1
        else:
            print("Gana el juego el jugador 2")
            p2 += 1

        cambio_saque()


def partido(sets):
    win = sets // 2 + 1
    p1 = 0
    p2 = 0
    while True:
        print(f"Sets: {p1} - {p2}")
        if p1 == win:
            return 1
        if p2 == win:
            return 2

        if set() == 1:
            print("################################################")
            print("Gana el set el jugador 1")
            print("################################################")
            p1 += 1
        else:
            print("################################################")
            print("Gana el set el jugador 2")
            print("################################################")
            p2 += 1


def main():
    print("Simulación de partido de tennis, el mejor de n sets.")
    print("No habrá tie-break, es decir, si un set llega a 6-6, se jugará hasta que un jugador gane por 2 juegos de diferencia.")

    print()

    try:
        sets = int(input("Ingrese el número de sets a simular (1,3,5): "))

        if sets not in [1, 3, 5]:
            print("Las únicas opciones válidas son 1, 3 y 5. Intente correrlo de nuevo.")
            return

    except:
        print("Las únicas opciones válidas son 1, 3 y 5. Intente correrlo de nuevo.")
        return

    print("*********************************")
    print(f"El partido será al mejor de {sets} sets")
    print(f"Empieza sacando el jugador {SAQUE}")
    print("*********************************")

    ganador = partido(sets)

    print("*********************************")
    print(f"El ganador del partido es el jugador {ganador}")
    print("*********************************")


main()
