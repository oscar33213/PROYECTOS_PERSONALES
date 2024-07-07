import os
import time
from playsound import playsound


def alarma(minutes, seconds):
    sound_path = os.path.join(os.path.dirname(__file__), "alarma_python.mp3")
    
    total_seconds = minutes * 60 + seconds
    
    print(f'La alarma sonara en {minutes} minutos y {seconds} segundos')
    
    time.sleep(total_seconds)
    
    playsound(sound_path)
    
minutes = int(input('Ingresa los minutos de la alarma: '))
seconds = int(input('Ingresa los segundos de la alarma: '))

alarma(minutes, seconds)
