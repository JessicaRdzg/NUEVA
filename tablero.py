import numpy as np
from variables import DIMENSIONES_TABLERO, BARCOS

class Tablero:
    def __init__(self, jugador_id):
        self.jugador_id = jugador_id
        self.dimensiones_tablero = DIMENSIONES_TABLERO
        self.barcos = BARCOS
        self.tablero_barcos = np.zeros((self.dimensiones_tablero, self.dimensiones_tablero), dtype=int)
        self.tablero_disparos = np.zeros((self.dimensiones_tablero, self.dimensiones_tablero), dtype=str)
        self.inicializar_tablero()

    def inicializar_tablero(self):
        # Colocar los barcos en el tablero
        for barco, eslora in self.barcos.items():
            self.colocar_barco(barco, eslora)

    def colocar_barco(self, nombre_barco, eslora):
        # Colocar un barco en el tablero
        colocar = False
        while not colocar:
            fila = np.random.randint(self.dimensiones_tablero)
            columna = np.random.randint(self.dimensiones_tablero)
            direccion = np.random.choice(['horizontal', 'vertical'])

            if direccion == 'horizontal':
                if columna + eslora <= self.dimensiones_tablero and np.all(self.tablero_barcos[fila, columna:columna+eslora] == 0):
                    self.tablero_barcos[fila, columna:columna+eslora] = 1
                    colocar = True
            else:
                if fila + eslora <= self.dimensiones_tablero and np.all(self.tablero_barcos[fila:fila+eslora, columna] == 0):
                    self.tablero_barcos[fila:fila+eslora, columna] = 1
                    colocar = True

    def disparar_coordenada(self, fila, columna):
        # Realizar un disparo en una coordenada
        if self.tablero_barcos[fila, columna] == 1:
            print("¡Impacto! Has alcanzado un barco.")
            self.tablero_disparos[fila, columna] = 'X'
        else:
            print("Agua. No has alcanzado ningún barco.")
            self.tablero_disparos[fila, columna] = 'O'

    def mostrar_tablero(self):
        # Mostrar el tablero con los barcos y los disparos
        print("Tablero del jugador", self.jugador_id)
        for fila in range(self.dimensiones_tablero):
            fila_str = ""
            for columna in range(self.dimensiones_tablero):
                if self.tablero_disparos[fila, columna] != '':
                    fila_str += self.tablero_disparos[fila, columna]
                else:
                    fila_str += str(self.tablero_barcos[fila, columna])
            print(fila_str)

# Ejemplo de uso
if __name__ == "__main__":
    tablero_jugador1 = Tablero(1)
    tablero_jugador1.mostrar_tablero()

    # Ejemplo de disparo
    tablero_jugador1.disparar_coordenada(0, 0)
    tablero_jugador1.mostrar_tablero()
