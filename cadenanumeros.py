
numeros = (int(input("INDICA EL NUMERO, ESTE TIENE QUE SER POSITIVO: ")))
suma = 0
while numeros >= 0:
    suma = suma + numeros
    numeros = (int(input("INDICA EL NUMERO, ESTE TIENE QUE SER POSITIVO: ")))

print(f"La suma de los nuemros es: {suma}")