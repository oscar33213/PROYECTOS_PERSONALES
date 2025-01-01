import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self):
        self.notas = []

    def agregarNota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def mostrarNotas(self):
        return "\n".join(map(str, self.notas))

    def mostrarPromedio(self):
        return f"El promedio de las notas es: {self.promedio():.2f}"

    def mostrarNotaMayor(self):
        return f"La nota mayor es: {max(self.notas)}" if self.notas else "No hay notas registradas."

    def mostrarNotaMenor(self):
        return f"La nota menor es: {min(self.notas)}" if self.notas else "No hay notas registradas."

    def mostrarCantidadNotas(self):
        return f"La cantidad de notas es: {len(self.notas)}"

    def mostrarCantidadNotasAprobadas(self):
        return f"La cantidad de notas aprobadas es: {len([nota for nota in self.notas if nota >= 4])}"

    def mostrarCantidadNotasReprobadas(self):
        return f"La cantidad de notas reprobadas es: {len([nota for nota in self.notas if nota < 4])}"

    def mostrarCantidadNotasSuficientes(self):
        return f"La cantidad de notas suficientes es: {len([nota for nota in self.notas if nota >= 6])}"

    def mostrarCantidadNotasInsuficientes(self):
        return f"La cantidad de notas insuficientes es: {len([nota for nota in self.notas if nota < 6])}"

    def verificarAprobacion(self):
        return "Has pasado de curso!" if self.promedio() >= 5 else "No has pasado de curso."

# Funciones para Tkinter
def agregar_nota():
    try:
        nota = float(entry_nota.get())
        if 0 <= nota <= 10:
            notas.agregarNota(nota)
            entry_nota.delete(0, tk.END)
            actualizar_informacion()
        else:
            messagebox.showerror("Error", "Por favor, ingresa una nota válida entre 0 y 10.")
    except ValueError:
        messagebox.showerror("Error", "Entrada inválida. Por favor, ingresa un número.")

def actualizar_informacion():
    text_info.delete(1.0, tk.END)
    text_info.insert(tk.END, notas.mostrarNotas() + "\n\n")
    text_info.insert(tk.END, notas.mostrarPromedio() + "\n")
    text_info.insert(tk.END, notas.mostrarNotaMayor() + "\n")
    text_info.insert(tk.END, notas.mostrarNotaMenor() + "\n")
    text_info.insert(tk.END, notas.mostrarCantidadNotas() + "\n")
    text_info.insert(tk.END, notas.mostrarCantidadNotasAprobadas() + "\n")
    text_info.insert(tk.END, notas.mostrarCantidadNotasReprobadas() + "\n")
    text_info.insert(tk.END, notas.mostrarCantidadNotasSuficientes() + "\n")
    text_info.insert(tk.END, notas.mostrarCantidadNotasInsuficientes() + "\n\n")
    text_info.insert(tk.END, notas.verificarAprobacion())

# Configuración de la ventana principal
notas = Notas()
root = tk.Tk()
root.title("Gestor de Notas")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_nota = tk.Label(frame, text="Ingresa una nota:")
label_nota.grid(row=0, column=0, padx=5, pady=5)

entry_nota = tk.Entry(frame)
entry_nota.grid(row=0, column=1, padx=5, pady=5)

btn_agregar = tk.Button(frame, text="Agregar Nota", command=agregar_nota)
btn_agregar.grid(row=0, column=2, padx=5, pady=5)

text_info = tk.Text(root, width=50, height=20)
text_info.pack(padx=10, pady=10)

actualizar_informacion()

root.mainloop()
