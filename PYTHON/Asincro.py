import asyncio

async def suma_con_retraso(a, b, segundos):
    await asyncio.sleep(segundos)
    return a + b

async def main():
    # Ejemplo de uso de la función de suma con retraso
    tareas = [
        suma_con_retraso(1, 2, 3),  # suma 1 + 2 y espera 3 segundos
        suma_con_retraso(4, 5, 2),  # suma 4 + 5 y espera 2 segundos
        suma_con_retraso(7, 8, 1),  # suma 7 + 8 y espera 1 segundo
    ]

    # Espera a que todas las tareas finalicen
    resultados = await asyncio.gather(*tareas)

    # Muestra los resultados
    for i, resultado in enumerate(resultados):
        print(f"Resultado de la tarea {i+1}: {resultado}")

# Ejecuta el programa principal
asyncio.run(main())
