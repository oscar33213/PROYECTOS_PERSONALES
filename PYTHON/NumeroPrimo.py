import math as m

numeroPrimo = int(input("Indique el numero a evaluar: "))


def esPrimo(numero):
    if numero < 2:
        return False
    else:
        for i in range(2, int(m.sqrt(numero)) + 1):
            if numero % i == 0:
                return 'No es primo'
        return 'Es primo'


print(esPrimo(numeroPrimo))


