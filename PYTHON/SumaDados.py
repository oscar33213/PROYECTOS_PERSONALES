
import random

ResultadoDados = []

SumaResultados = 0

for i in range(20):
    ResultadoDados.append(random.randint(1,6))


def SumaDados():
    global SumaResultados
    for i in ResultadoDados:
        SumaResultados += i
    return SumaResultados



print(ResultadoDados)


print(SumaDados())

