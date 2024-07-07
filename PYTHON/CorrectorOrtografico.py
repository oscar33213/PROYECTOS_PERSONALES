from autocorrect import Speller

spell = Speller(lang='es')

def corregir_palabra(word):
    corregida = spell(word)
    return corregida if corregida != word else word

def corregir_frase(frase):
    palabras = frase.split()
    palabras_corregidas = [corregir_palabra(palabra) for palabra in palabras]
    frase_corregida = ' '.join(palabras_corregidas)
    return frase_corregida

frase = input("Indica la palabra o frase: ")    
print(corregir_frase(frase))

