from autocorrect import Speller


spell = Speller(lang='es')

def corregir_palabra(word):
    
    if not spell(word) == word:
        return spell(word)
    else:
        return word
    

palabra = input("Indica la palabra o frase: ")    

print(corregir_palabra(palabra))
