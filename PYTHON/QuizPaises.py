import random

capitals = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Alemania": "Berlín",
    "Rusia": "Moscú",
    "Inglaterra": "Londres",
    "Portugal": "Lisboa",
    "Suiza": "Berna",
    "Grecia": "Atenas",
    "Bélgica": "Bruselas",
    "Países Bajos": "Ámsterdam",
    "Dinamarca": "Copenhague",
    "Suecia": "Estocolmo",
    "Noruega": "Oslo",
    "Finlandia": "Helsinki",
    "Polonia": "Varsovia",
    "Austria": "Viena",
    "Hungría": "Budapest",
    "República Checa": "Praga",
    "Irlanda": "Dublín",
    "Estados Unidos": "Washington D.C.",
    "Canadá": "Ottawa",
    "México": "Ciudad de México",
    "Brasil": "Brasilia",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Australia": "Canberra",
    "Nueva Zelanda": "Wellington",
    "Japón": "Tokio",
    "China": "Pekín",
    "India": "Nueva Delhi",
    "Sudáfrica": "Pretoria",
    "Egipto": "El Cairo",
    "Nigeria": "Abuya",
    "Turquía": "Ankara",
    "Arabia Saudita": "Riad",
    "Israel": "Jerusalén",
    "Corea del Sur": "Seúl",
    "Indonesia": "Yakarta",
    "Vietnam": "Hanói",
    "Tailandia": "Bangkok",
    "Filipinas": "Manila"
}

def quiz_capitals():
    print("Bienvenido al cuestionario de capitales")
    score = 0
    vidas = 5

    # Obtener una lista de los países y capitales y randomizar el orden
    items = list(capitals.items())
    random.shuffle(items)
    
    for country, capital in items:
        print(f'¿Cuál es la capital de {country}?')
        user_answer = input("Indica respuesta: ")
        
        if user_answer.lower() == capital.lower():
            print('¡CORRECTO!')
            score += 1
        else:
            print(f'¡Error! La capital de {country} es: {capital}')
            vidas = vidas - 1
            print(f'Te quedan: {vidas} vidas')
            
        if vidas <= 0:
            print(f'Has perdido, tu puntuación final es de: {score} puntos')
            return  # Salir de la función si se han agotado las vidas
    
    # Si aún quedan vidas al finalizar el cuestionario
    print(f'¡Felicidades! Has completado el cuestionario con {score} puntos.')

# Ejemplo de uso
quiz_capitals()


