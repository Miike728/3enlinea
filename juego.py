# FILEPATH: a

import random

# Tablero de juego
tablero = [' '] * 9

# Símbolos de los jugadores
jugador = 'X'
ia = 'O'

# Función para imprimir el tablero
def imprimir_tablero():
    print('-------------')
    print('|', tablero[0], '|', tablero[1], '|', tablero[2], '|')
    print('-------------')
    print('|', tablero[3], '|', tablero[4], '|', tablero[5], '|')
    print('-------------')
    print('|', tablero[6], '|', tablero[7], '|', tablero[8], '|')
    print('-------------')

# Función para verificar si alguien ha ganado
def verificar_ganador(tablero, jugador):
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]  # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

# Función para que la IA realice un movimiento
def movimiento_ia(tablero):
    # Buscar una casilla vacía aleatoriamente
    casillas_vacias = [i for i in range(9) if tablero[i] == ' ']
    movimiento = random.choice(casillas_vacias)
    tablero[movimiento] = ia

# Función principal del juego
def jugar():
    imprimir_tablero()
    while True:
        # Turno del jugador
        movimiento_jugador = int(input("Elige una casilla (0-8): "))
        if tablero[movimiento_jugador] == ' ':
            tablero[movimiento_jugador] = jugador
        else:
            print("Casilla ocupada. Intenta de nuevo.")
            continue

        imprimir_tablero()

        if verificar_ganador(tablero, jugador):
            print("¡Has ganado!")
            break

        # Turno de la IA
        movimiento_ia(tablero)
        imprimir_tablero()

        if verificar_ganador(tablero, ia):
            print("¡La IA ha ganado!")
            break

        # Verificar si hay empate
        if ' ' not in tablero:
            print("¡Empate!")
            break

# Iniciar el juego
jugar()
