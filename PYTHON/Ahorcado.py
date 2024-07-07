import random

sourceDir = "F:/PROYECTOS_PYTHON_PERSONALES/PYTHON/ahoracadojuego/peliculas.txt"

with open (sourceDir, 'r') as f:
    words = f.readlines()
    
    word = random.choice(words).strip()
    
    errors = 4
    intentGuess = []
    run = True
    
    
while run:
    # Mostrar el estado actual de la palabra
    for letter in word:
        if letter.lower() in intentGuess:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print("\n")
    
    # Pedir una nueva letra al jugador
    intent = input(f'Errors left {errors}. Next try: ').strip().lower()
    
    # Comprobar si la letra ya fue adivinada
    if intent in intentGuess:
        print("You already tried that letter. Try a different one.")
        continue
    
    # Añadir la letra adivinada a la lista de intentos
    intentGuess.append(intent)
    
    # Comprobar si la letra no está en la palabra
    if intent not in word.lower():
        errors = errors - 1
        print(f'You have {errors} intents left')
        
        if errors == 0:
            print(f'You have {errors} intents. You lost :(')
            print(f'The word was: {word}')
            break
    
    # Comprobar si todas las letras de la palabra han sido adivinadas
    run = False
    for letter in word:
        if letter.lower() not in intentGuess:
            run = True

if not run:
    print(f'Correct word! It was {word}')
    
    
    input('Presiona uuna tecla para salir')