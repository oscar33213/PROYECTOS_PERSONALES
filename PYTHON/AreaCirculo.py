import math as m
from tkinter import *



def Area_Circulo():
    
    #Pi * r*2
    try:
        radio = float(cuadroRadio.get())
        pi = m.pi
        aresCirculo = (pi * m.pow(radio, 2))
        resultado.set(f"El area del circulo con {radio} de radio es: {aresCirculo}")
        
    except:
        return "Introduzca un radio valido"
    
    


raiz = Tk()
raiz.title("Area Circulo")


miFrame = Frame(raiz, width=1200, height=800)
miFrame.pack()


Label(miFrame, text="Radio").grid(row=0, column=0)
cuadroRadio = Entry(miFrame)
cuadroRadio.grid(row=1, column=1)


resultado = StringVar()


Label(miFrame, textvariable=resultado).grid(row=3, columnspan=2)



botonCalcular = Button(miFrame, text="Calcular", command=Area_Circulo)
botonCalcular.grid(row=2, columnspan=2)

# Run the main loop
raiz.mainloop()

