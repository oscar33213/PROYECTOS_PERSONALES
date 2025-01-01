import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class BaseDeDatos:
    def __init__(self):
        self.datos = []

    def agregar_registro(self, nombre, puesto, correo, hora_entrada, hora_salida):
        registro = {
            "nombre": nombre,
            "puesto": puesto,
            "correo": correo,
            "hora_entrada": hora_entrada,
            "hora_salida": hora_salida
        }
        self.datos.append(registro)

    def ver_todos(self):
        return self.datos

    def buscar_por_nombre(self, nombre):
        return [registro for registro in self.datos if registro["nombre"].lower() == nombre.lower()]

    def eliminar_por_nombre(self, nombre):
        inicial = len(self.datos)
        self.datos = [registro for registro in self.datos if registro["nombre"].lower() != nombre.lower()]
        eliminados = inicial - len(self.datos)
        return eliminados


class Aplicacion:
    def __init__(self, root):
        self.bd = BaseDeDatos()
        self.root = root
        self.root.title("Registro de Empleados")

        # Crear los elementos de la interfaz gráfica
        self.nombre_label = tk.Label(root, text="Nombre:")
        self.nombre_label.grid(row=0, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1)

        self.puesto_label = tk.Label(root, text="Puesto de Trabajo:")
        self.puesto_label.grid(row=1, column=0)
        self.puesto_entry = tk.Entry(root)
        self.puesto_entry.grid(row=1, column=1)

        self.correo_label = tk.Label(root, text="Correo Electrónico:")
        self.correo_label.grid(row=2, column=0)
        self.correo_entry = tk.Entry(root)
        self.correo_entry.grid(row=2, column=1)

        self.entrada_label = tk.Label(root, text="Hora de Entrada (HH:MM):")
        self.entrada_label.grid(row=3, column=0)
        self.entrada_entry = tk.Entry(root)
        self.entrada_entry.grid(row=3, column=1)

        self.salida_label = tk.Label(root, text="Hora de Salida (HH:MM):")
        self.salida_label.grid(row=4, column=0)
        self.salida_entry = tk.Entry(root)
        self.salida_entry.grid(row=4, column=1)

        self.agregar_btn = tk.Button(root, text="Agregar registro", command=self.agregar_registro)
        self.agregar_btn.grid(row=5, column=0, columnspan=2)

        self.ver_btn = tk.Button(root, text="Ver todos los registros", command=self.ver_todos)
        self.ver_btn.grid(row=6, column=0, columnspan=2)

        self.buscar_label = tk.Label(root, text="Buscar por nombre:")
        self.buscar_label.grid(row=7, column=0)
        self.buscar_entry = tk.Entry(root)
        self.buscar_entry.grid(row=7, column=1)
        self.buscar_btn = tk.Button(root, text="Buscar", command=self.buscar_por_nombre)
        self.buscar_btn.grid(row=8, column=0, columnspan=2)

        self.eliminar_label = tk.Label(root, text="Eliminar por nombre:")
        self.eliminar_label.grid(row=9, column=0)
        self.eliminar_entry = tk.Entry(root)
        self.eliminar_entry.grid(row=9, column=1)
        self.eliminar_btn = tk.Button(root, text="Eliminar", command=self.eliminar_por_nombre)
        self.eliminar_btn.grid(row=10, column=0, columnspan=2)

        self.resultados_text = tk.Text(root, height=10, width=50)
        self.resultados_text.grid(row=11, column=0, columnspan=2)

    def agregar_registro(self):
        nombre = self.nombre_entry.get()
        puesto = self.puesto_entry.get()
        correo = self.correo_entry.get()
        hora_entrada = self.entrada_entry.get()
        hora_salida = self.salida_entry.get()

        # Verificar formato de hora
        try:
            datetime.strptime(hora_entrada, "%H:%M")
            datetime.strptime(hora_salida, "%H:%M")
        except ValueError:
            messagebox.showwarning("Advertencia", "El formato de hora debe ser HH:MM.")
            return

        if nombre and puesto and correo and hora_entrada and hora_salida:
            self.bd.agregar_registro(nombre, puesto, correo, hora_entrada, hora_salida)
            messagebox.showinfo("Éxito", "Registro agregado correctamente.")
        else:
            messagebox.showwarning("Advertencia", "Debe llenar todos los campos.")

    def ver_todos(self):
        registros = self.bd.ver_todos()
        self.mostrar_resultados(registros)

    def buscar_por_nombre(self):
        nombre = self.buscar_entry.get()
        if nombre:
            resultados = self.bd.buscar_por_nombre(nombre)
            self.mostrar_resultados(resultados)
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre para buscar.")

    def eliminar_por_nombre(self):
        nombre = self.eliminar_entry.get()
        if nombre:
            eliminados = self.bd.eliminar_por_nombre(nombre)
            if eliminados > 0:
                messagebox.showinfo("Éxito", f"{eliminados} registro(s) eliminado(s).")
            else:
                messagebox.showwarning("Advertencia", "No se encontraron registros para eliminar.")
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un nombre para eliminar.")

    def mostrar_resultados(self, registros):
        self.resultados_text.delete(1.0, tk.END)  # Limpiar el área de texto
        if registros:
            for registro in registros:
                self.resultados_text.insert(tk.END, f"Nombre: {registro['nombre']}, Puesto: {registro['puesto']}, "
                                                    f"Correo: {registro['correo']}, Entrada: {registro['hora_entrada']}, "
                                                    f"Salida: {registro['hora_salida']}\n")
        else:
            self.resultados_text.insert(tk.END, "No se encontraron registros.")


if __name__ == "__main__":
    root = tk.Tk()
    app = Aplicacion(root)
    root.mainloop()
