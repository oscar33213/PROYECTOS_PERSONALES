class BaseDeDatos:
    def __init__(self):
        self.datos = []

    def agregar_registro(self, nombre, edad, correo):
        registro = {
            "nombre": nombre,
            "edad": edad,
            "correo": correo
        }
        self.datos.append(registro)
        print(f"Registro agregado: {registro}")

    def ver_todos(self):
        if not self.datos:
            print("La base de datos está vacía.")
        else:
            for i, registro in enumerate(self.datos, start=1):
                print(f"{i}. {registro}")

    def buscar_por_nombre(self, nombre):
        resultados = [registro for registro in self.datos if registro["nombre"].lower() == nombre.lower()]
        if resultados:
            print("Registros encontrados:")
            for registro in resultados:
                print(registro)
        else:
            print("No se encontraron registros con ese nombre.")

    def eliminar_por_nombre(self, nombre):
        inicial = len(self.datos)
        self.datos = [registro for registro in self.datos if registro["nombre"].lower() != nombre.lower()]
        eliminados = inicial - len(self.datos)
        if eliminados > 0:
            print(f"{eliminados} registro(s) eliminado(s) con el nombre '{nombre}'.")
        else:
            print("No se encontraron registros con ese nombre para eliminar.")


if __name__ == "__main__":
    bd = BaseDeDatos()

    while True:
        print("\nOpciones:")
        print("1. Agregar registro")
        print("2. Ver todos los registros")
        print("3. Buscar por nombre")
        print("4. Eliminar por nombre")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            edad = input("Ingrese la edad: ")
            correo = input("Ingrese el correo: ")
            bd.agregar_registro(nombre, edad, correo)
        elif opcion == "2":
            bd.ver_todos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre a buscar: ")
            bd.buscar_por_nombre(nombre)
        elif opcion == "4":
            nombre = input("Ingrese el nombre a eliminar: ")
            bd.eliminar_por_nombre(nombre)
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
