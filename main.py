# from funciones import disparar_coordenada, comprobar_fin_juego
from tablero import Tablero

def main():
    print("¡Bienvenido a Hundir la Flota!")
    print("Instrucciones:")
    print("- Introduce las coordenadas para disparar en el tablero del oponente.")
    print("- El tablero se representa con números, donde 1 indica la presencia de un barco y 0 indica agua.")
    print("- Las coordenadas se introducen en formato fila-columna (por ejemplo, 1-1)")

    # Inicializar tableros de ambos jugadores
    tablero_jugador1 = Tablero(1)
    tablero_jugador2 = Tablero(2)

    # Inicializar variables de turno y fin del juego
    turno = 1
    fin_juego = False

    while not fin_juego:
        # Mostrar tablero del jugador actual
        print("\nTurno del Jugador", turno)
        if turno == 1:
            tablero_jugador1.mostrar_tablero()
        else:
            tablero_jugador2.mostrar_tablero()

        # Pedir coordenadas al jugador actual
        fila, columna = map(int, input("Introduce las coordenadas para disparar (fila-columna): ").split('-'))

        # Realizar disparo en el tablero del oponente
        if turno == 1:
            impacto = Tablero.disparar_coordenada(tablero_jugador2.tablero_barcos, fila-1, columna-1)
            if impacto:
                fin_juego = comprobar_fin_juego(tablero_jugador2.tablero_barcos)
        else:
            impacto = disparar_coordenada(tablero_jugador1.tablero_barcos, fila-1, columna-1)
            if impacto:
                fin_juego = comprobar_fin_juego(tablero_jugador1.tablero_barcos)

        # Cambiar turno
        turno = 3 - turno

    # Mostrar mensaje de fin del juego
    print("\n¡Fin del juego! Ha ganado el Jugador", turno)

if __name__ == "__main__":
    main()
