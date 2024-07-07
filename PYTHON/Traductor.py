from translate import Translator

def main():
    
    from_lang = input('Ingrese el idioma de origen (ej. spanish): ').strip().lower()
    to_lang = input('Ingrese el idioma de destino (ej. english): ').strip().lower()
    
    txt = input('¿Qué quieres traducir?: ')

    try:
        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        translation = translator.translate(txt)
        print(f'La palabra "{txt}" traducida a {to_lang.title()} es: {translation}')
    except ValueError:
        print('Error: Idiomas no soportados o ingresados incorrectamente.')

if __name__ == "__main__":
    main()

