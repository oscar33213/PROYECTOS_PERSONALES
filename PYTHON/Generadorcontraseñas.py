import random
import string

def generar_contraseña(longitud=12, usar_mayusculas=True, usar_minusculas=True, usar_digitos=True, usar_especiales=True):

    caracteres = ""
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_digitos:
        caracteres += string.digits
    if usar_especiales:
        caracteres += string.punctuation
    
    # Verificación temporal para depurar
    print(f"Caracteres seleccionados: {caracteres}")
    
    # Verificar que se haya seleccionado al menos un tipo de carácter
    if len(caracteres) == 0:
        raise ValueError("Debe seleccionarse al menos un tipo de carácter")
    
    # Generar la contraseña
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    
    longitud = int(input("Indica la longitud de la contraseña: "))
    
    usar_mayusculas = input("¿Incluir mayúsculas? (si/no): ").lower() == 'si'
    usar_minusculas = input("¿Incluir minúsculas? (si/no): ").lower() == 'si'
    usar_digitos = input("¿Incluir números? (si/no): ").lower() == 'si'
    usar_especiales = input("¿Incluir caracteres especiales? (si/no): ").lower() == 'si'
    
    contraseña = generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_digitos, usar_especiales)
    print(f"Contraseña generada: {contraseña}")

if __name__ == "__main__":
    main()
