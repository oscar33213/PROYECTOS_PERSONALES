
numeros = (int(input("INDICA EL NUMERO, ESTE TIENE QUE SER POSITIVO (SI INTRODUCES UN NUMERO NEGATIVO SE ACABA EL JUEGO): ")))
suma = 0
while numeros >= 0:
    suma = suma + numeros
    numeros = (int(input("INDICA EL NUMERO, ESTE TIENE QUE SER POSITIVO (SI INTRODUCES UN NUMERO NEGATIVO SE ACABA EL JUEGO): ")))

print(f"La suma de los nuemros es: {suma}")