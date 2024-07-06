import os
import time

def DameHora():
    return time.strftime("%H:%M:%S")

try:
    while True:
        hora = DameHora()
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        print(hora)
        time.sleep(1)
except KeyboardInterrupt:
    print("Program terminated.")
