import subprocess

perfil_red = input('Introiduce el nombre de red Wi-Fi: ')

try:
    resultados = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil_red, 'key=clear'],
                                        shell=True).decode('utf-8', errors='backslashreplace')
    
    
    
    if 'Contendio de la clave' in resultados:
        for line in resultados.split('\n'):
            if 'Contenido de la clave' in line:
                password = line.split(':')[1].strip()
                print(f'La contraseña dela red {perfil_red} es: {password}')
                break
            
    else:
        print(f'No se pudo encntar la contarseña para la red {perfil_red}')
        

except subprocess.CalledProcessError:
    print(f'No se pudo obtener la información de la red {perfil_red}')
    
 
 
input('Presione cualquier tecla para salir')
    
