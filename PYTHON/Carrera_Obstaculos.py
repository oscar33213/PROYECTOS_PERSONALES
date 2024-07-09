def evaluar_carrera(acciones, pista):
    pista_lista = list(pista)
    longitud_pista = len(pista)
    
    if len(acciones) != longitud_pista:
        raise ValueError("La longitud de las acciones debe coincidir con la longitud de la pista.")

    carrera_superada = True
    
    for i in range(longitud_pista):
        if pista_lista[i] == "_":
            if acciones[i] == "run":
                pass  # Correcto
            elif acciones[i] == "jump":
                pista_lista[i] = "x"
                carrera_superada = False
        elif pista_lista[i] == "|":
            if acciones[i] == "jump":
                pass  # Correcto
            elif acciones[i] == "run":
                pista_lista[i] = "/"
                carrera_superada = False
    
    pista_modificada = "".join(pista_lista)
    print(f"Pista final: {pista_modificada}")
    return carrera_superada

# Ejemplo de uso
acciones = ["run", "jump", "run", "run", "jump"]
pista = "_|__|"

resultado = evaluar_carrera(acciones, pista)
print(f"Carrera superada: {resultado}")
