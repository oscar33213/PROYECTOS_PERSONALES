from tkinter import *

def CalculadoraICM():
    try:
        peso = float(cuadroPeso.get())
        altura = float(cuadroaltura.get())
        bmi = peso / (altura ** 2)
        resultado.set(f"BMI: {bmi:.2f}")
    except ValueError:
        resultado.set("Please enter valid numbers")

# Initialize the main window
raiz = Tk()
raiz.title("Calculadora de ICM")

# Create a frame inside the main window
miFrame = Frame(raiz, width=100, height=600)
miFrame.pack()

# Create and place the input fields for weight and height
Label(miFrame, text="Peso (kg)").grid(row=0, column=0)
cuadroPeso = Entry(miFrame)
cuadroPeso.grid(row=0, column=1)

Label(miFrame, text="Altura (m)").grid(row=1, column=0)
cuadroaltura = Entry(miFrame)
cuadroaltura.grid(row=1, column=1)

# Create a variable to store the result
resultado = StringVar()

# Create and place a label to display the result
Label(miFrame, textvariable=resultado).grid(row=3, columnspan=2)

# Create and place the Calculate button
botonCalcular = Button(miFrame, text="Calcular", command=CalculadoraICM)
botonCalcular.grid(row=2, columnspan=2)

# Run the main loop
raiz.mainloop()
