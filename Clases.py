class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombreP = nombre
        self.apellidoP = apellido
        self.edadP = edad
        
        
    
    def Saludar(self):
        
        return f"Hola. Te llamas: {self.nombreP}, con apellido: {self.apellidoP} y tienes: {self.edadP} años"
        
        
    
    def Acceso(self, edad):
        if edad < 18:
            return "Lo siento, no puedes pasar"  
        elif edad < 65:  # No es necesario verificar 'edad >= 18' porque la primera condición ya lo excluye
            return "Puedes pasar"
        else:
            return "Puedes pasar con descuento"
        
persona1 = Persona("Oscar", "Hidalgo", 27)
        
print(persona1.Saludar())
print(persona1.Acceso(32))