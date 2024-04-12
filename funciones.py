import numpy as np
from variables import DIMENSIONES_TABLERO, BARCOS

def colocar_barco(tablero, nombre_barco, eslora):
    # Colocar un barco en el tablero
    colocar = False
    while not colocar:
        fila = np.random.randint(DIMENSIONES_TABLERO)
        columna = np.random.randint(DIMENSIONES_TABLERO)
        direccion = np.random.choice(['horizontal', 'vertical'])

        if direccion == 'horizontal':
            if columna + eslora <= DIMENSIONES_TABLERO and np.all(tablero[fila, columna:columna+eslora] == 0):
                tablero[fila, columna:columna+eslora] = 1
                colocar = True
        else:
            if fila + eslora <= DIMENSIONES_TABLERO and np.all(tablero[fila:fila+eslora, columna] == 0):
                tablero[fila:fila+eslora, columna] = 1
                colocar = True

def disparar_coordenada(tablero, fila, columna):
    # Realizar un disparo en una coordenada
    if tablero[fila, columna] == 1:
        print("¡Impacto! Has alcanzado un barco.")
        tablero[fila, columna] = 'X'
        return True
    else:
        print("Agua. No has alcanzado ningún barco.")
        return False

def comprobar_fin_juego(tablero):
    # Comprobar si se ha acabado el juego
    return np.sum(tablero) == 0
