from translate import Translator

translator = Translator(from_lang='spanish', to_lang='english')

txt = input('¿Qué quieres traducir: ')

res = translator.translate(txt)

print(f'La palabra {txt} traducida al Ingles es: {res}')

