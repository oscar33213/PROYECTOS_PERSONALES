from random import randint

def juego():
    eleccion = ["Piedra", "Papel", "Tijera"]
    puntuacion = 0
    vidas = 5

    while vidas > 0:
        bot = eleccion[randint(0, 2)]
        print("\nElige: (Piedra) (Papel) (Tijera)")
        jugador = input().lower()
        print("La máquina ha elegido: " + bot)

        # JUEGO
        if jugador == bot:
            print("Empate")
        elif jugador == "tijera" and bot == "Papel":
            print("Tú ganas")
            puntuacion += 1
        elif jugador == "tijera" and bot == "Piedra":
            print("Tú pierdes")
            vidas -= 1
            print("Te quedan: " + str(vidas) + " vidas")
        elif jugador == "papel" and bot == "Tijera":
            print("Tú pierdes")
            vidas -= 1
            print("Te quedan: " + str(vidas) + " vidas")
        elif jugador == "papel" and bot == "Piedra":
            print("Tú ganas")
            puntuacion += 1
        elif jugador == "piedra" and bot == "Papel":
            print("Tú pierdes")
            vidas -= 1
            print("Te quedan: " + str(vidas) + " vidas")
        elif jugador == "piedra" and bot == "Tijera":
            print("Tú ganas")
            puntuacion += 1

    # Al quedarse sin vidas
    print("\nEl juego se ha terminado, has conseguido: " + str(puntuacion) + " puntos")
    volver_a_jugar = input("¿Quieres volver a jugar? (sí/no): ").lower()

    if volver_a_jugar == "sí" or volver_a_jugar == "si":
        juego()  # Reinicia el juego
    else:
        print("Gracias por jugar. ¡Hasta la próxima!")

# Inicia el juego
print("Bienvenido al juego de Piedra, Papel o Tijera \n")
juego()



