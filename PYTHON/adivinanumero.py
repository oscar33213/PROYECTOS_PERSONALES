import random
vidas = 5
numeroAAdivinar = random.randint(0, 100)

run = True

while run:
    numeroElegido = int(input('Escoge un número entre 0 y 100: '))
    
    if numeroAAdivinar == numeroElegido:
        print(f'¡Enhorabuena, has acertado! El número era: {numeroAAdivinar}')
        run = False
    elif numeroAAdivinar > numeroElegido:
        vidas -= 1
        print(f'El número {numeroElegido} es menor al número a adivinar')
        print(f'Te quedan: {vidas} vidas')
    else:
        vidas -= 1
        print(f'El número {numeroElegido} es mayor al número a adivinar')
        print(f'Te quedan: {vidas} vidas')
    
    if vidas == 0:
        run = False
        print(f'Has perdido, te quedan 0 vidas. El número era: {numeroAAdivinar}')
