from textblob import TextBlob

def analyze_sentiments(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = 'Positivo'
    elif polarity < 0:
        sentiment = 'Negativo'
    else:
        sentiment = 'Neutral'
    
    print(f'Texto: {text}')
    print(f'Polaridad: {polarity}')
    print(f'Sentimiento: {sentiment}')

# Programa principal
def main():
    while True:
        text_example = input('Indica una frase para analizar el sentimiento (o "exit" para salir): ')
        
        if text_example.lower() == 'exit':
            print('Saliendo del programa...')
            break
        
        analyze_sentiments(text_example)
        print()  # Separación visual entre resultados

# Ejecutar el programa principal
if __name__ == "__main__":
    main()



input('Presiona uuna tecla para salir')