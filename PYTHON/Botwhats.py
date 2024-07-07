import pywhatkit
from datetime import datetime
import time
import random

# Lista de posibles mensajes
posibles_mensajes = [
    'Hola, ¿cómo estás?',
    '¡Feliz cumpleaños!',
    'Nos vemos mañana a las 10.',
    'Reunión confirmada para el lunes.',
    'Espero que tengas un buen día.',
    'No olvides la reunión de hoy.',
    '¡Buen trabajo con el proyecto!',
    'Te llamaré más tarde.'
]

# Lista de números de teléfono
numeros = []

# Tiempo actual más 60 segundos
seconds = time.time() + 60
date = datetime.fromtimestamp(seconds)

# Enviar mensajes
for numero in numeros:
    mensaje = random.choice(posibles_mensajes)  # Seleccionar un mensaje aleatorio
    pywhatkit.sendwhatmsg(numero, mensaje, date.hour, date.minute)
    time.sleep(5)  # Asegura un intervalo de 5 segundos entre cada mensaje
