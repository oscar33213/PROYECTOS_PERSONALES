

# PROGRAMA PARA CREAR UN CORREO CON EL MISMO NOMBRE X VECES 
# EL PROGRAMA ARROJARA LO SIGUIENTE: "tunombre1@gmail.com, tunombre2@gmail.com ASI EL NUMERO DE VECES INDICADO"

nombre = input("INTRODUCE TU NOMBRE: ")
veces = int(input("INDICA EL NUMERO DE VECES QUE SE REPETIRA EL NUMERO: "))


for i in range(veces):
    print(f"{nombre}{i + 1}@gmail.com")
    
    
    