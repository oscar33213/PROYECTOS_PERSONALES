
import requests
from bs4 import BeautifulSoup


for num in range (15, 30):

    url = input(f'Indica la URL completa: ')

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        
        soup = BeautifulSoup(respuesta.text, 'html.parser')
        word = input('Indica la palabra a buscar: ')
        
        
        if word in soup.get_text().lower():
            print(f'La palabra {word}, se encuentra en la url {url}')
            
        else: 
            print('Error. no se puede acceder a la pagina')