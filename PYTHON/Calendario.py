import tkinter as tk
from tkcalendar import Calendar
import os 
import datetime as dt

def print_date():
    selected_date = cal.selection_get()
    date_label.config(text=f'Fecha seleccionada: {selected_date}')


fechaActual = dt.date.today()


root = tk.Tk()
root.title('Calendario')



cal = Calendar(root, selectmode = 'day', year = fechaActual.year, month = fechaActual.month, day = fechaActual.day)
cal.pack(pady = 20)

tk.Button(root, text='Selecciona Fecha', command=print_date).pack(pady=20)


miframe = tk.Frame(root)
miframe.pack(pady=20)

# Etiqueta para mostrar la fecha seleccionada
date_label = tk.Label(miframe, text="Fecha seleccionada: Ninguna")
date_label.pack()

input('Presiona uuna tecla para salir')

root.mainloop()

