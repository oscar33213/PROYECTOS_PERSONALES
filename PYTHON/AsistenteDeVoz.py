import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def talk():
    mic = sr.Microphone()
    with mic as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f'Has dicho: {text}')
        return text.lower()
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
        return ""
    except sr.RequestError:
        print("Error al comunicarse con el servicio de reconocimiento")
        return ""

if 'amazon' in talk():
    engine.say('¿Qué quieres comprar en Amazon?')
    engine.runAndWait()
    text = talk()
    
    if text:
        webbrowser.open(f'https://www.amazon.es/s?k={text}')


input('Presiona uuna tecla para salir')