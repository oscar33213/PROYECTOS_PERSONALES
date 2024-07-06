import os
shutdown = input('¿Quieres apagar el ordenador? (S/N)')

if shutdown.lower()== 's':
    os.system('shutdown /s /t 1')
else:
    exit()
    
    
    