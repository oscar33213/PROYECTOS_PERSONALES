from rembg import remove
from PIL import Image


removeBG = remove(Image.open('imagen.jpg'))
removeBG.save('imagenSinFondo.png')
print('Fondo eliminado')
