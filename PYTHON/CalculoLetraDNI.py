

dniUsuario = input("Introduce tu numero de DNI sin letra: ")


def SacarLetraDNI(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    return letras[int(dni) % 23]

DNIConLetra = SacarLetraDNI(dniUsuario)
print(f"La letra de tu DNI es: {SacarLetraDNI(dniUsuario)}")

print (f"Tu DNI completo es: {dniUsuario}{DNIConLetra}")



