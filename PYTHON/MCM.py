
numeroA = int(input("Indique el primer numero a evaluar: "))
numeroB = int(input("Indique el segundo numero a evaluar: "))

def SacaMCM(numeroA, numeroB):
    if numeroA > numeroB:
        mayor = numeroA
    else:
        mayor = numeroB
    while True:
        if mayor % numeroA == 0 and mayor % numeroB == 0:
            return mayor
        mayor += 1
        
        

print(SacaMCM(numeroA, numeroB))