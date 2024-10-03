def juego():
    puntuacion_jugador1 = 0
    puntuacion_jugador2 = 0
    vidas_jugador1 = 5
    vidas_jugador2 = 5

    while vidas_jugador1 > 0 and vidas_jugador2 > 0:
        print("\nJugador 1, elige: (Piedra) (Papel) (Tijera)")
        jugador1 = input().lower()

        print("\nJugador 2, elige: (Piedra) (Papel) (Tijera)")
        jugador2 = input().lower()

        print("\nJugador 1 ha elegido: " + jugador1.capitalize())
        print("Jugador 2 ha elegido: " + jugador2.capitalize())

        # JUEGO
        if jugador1 == jugador2:
            print("Empate")
        elif jugador1 == "tijera" and jugador2 == "papel":
            print("Jugador 1 gana")
            puntuacion_jugador1 += 1
            vidas_jugador2 -= 1
            print("Jugador 2 pierde una vida. Le quedan: " + str(vidas_jugador2) + " vidas")
        elif jugador1 == "tijera" and jugador2 == "piedra":
            print("Jugador 2 gana")
            puntuacion_jugador2 += 1
            vidas_jugador1 -= 1
            print("Jugador 1 pierde una vida. Le quedan: " + str(vidas_jugador1) + " vidas")
        elif jugador1 == "papel" and jugador2 == "tijera":
            print("Jugador 2 gana")
            puntuacion_jugador2 += 1
            vidas_jugador1 -= 1
            print("Jugador 1 pierde una vida. Le quedan: " + str(vidas_jugador1) + " vidas")
        elif jugador1 == "papel" and jugador2 == "piedra":
            print("Jugador 1 gana")
            puntuacion_jugador1 += 1
            vidas_jugador2 -= 1
            print("Jugador 2 pierde una vida. Le quedan: " + str(vidas_jugador2) + " vidas")
        elif jugador1 == "piedra" and jugador2 == "papel":
            print("Jugador 2 gana")
            puntuacion_jugador2 += 1
            vidas_jugador1 -= 1
            print("Jugador 1 pierde una vida. Le quedan: " + str(vidas_jugador1) + " vidas")
        elif jugador1 == "piedra" and jugador2 == "tijera":
            print("Jugador 1 gana")
            puntuacion_jugador1 += 1
            vidas_jugador2 -= 1
            print("Jugador 2 pierde una vida. Le quedan: " + str(vidas_jugador2) + " vidas")

    # Al quedarse uno de los jugadores sin vidas
    if vidas_jugador1 == 0:
        print("\nJugador 1 se ha quedado sin vidas. Jugador 2 gana con " + str(puntuacion_jugador2) + " puntos")
    elif vidas_jugador2 == 0:
        print("\nJugador 2 se ha quedado sin vidas. Jugador 1 gana con " + str(puntuacion_jugador1) + " puntos")

    volver_a_jugar = input("¿Quieren volver a jugar? (sí/no): ").lower()

    if volver_a_jugar == "sí" or volver_a_jugar == "si":
        juego()  # Reinicia el juego
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

# Inicia el juego
print("Bienvenidos al juego de Piedra, Papel o Tijera \n")
juego()
