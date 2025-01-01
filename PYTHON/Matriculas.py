

import random as rd

def generar_matriculas():
    
    letras_permitidas = "BCDFGHJKLMNPQRSTVWXYZ"
    
    numeros = f"{rd.randint(0, 9999):04d}"
    
    
    letras = "".join(rd.choices(letras_permitidas, k=3))
    
    
    matricula = f"{numeros}{letras}"
    
    return matricula


matriculas = [generar_matriculas() for _ in range(10)]

print(matriculas)

