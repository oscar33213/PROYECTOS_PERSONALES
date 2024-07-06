import speech_recognition as sr

recognizer = sr.Recognizer()


with sr.Microphone() as source:
    print("Por favor, hable ahora...")
    
    
    recognizer.adjust_for_ambient_noise(source)
    
    
    audio = recognizer.listen(source)
    
    try:
        
        text = recognizer.recognize_google(audio, language='es-ES')
        print(f'Has dicho: {text}')
    except sr.UnknownValueError:
        print("No se pudo entender el audio")
    except sr.RequestError as e:
        print(f"No se pudo solicitar los resultados del servicio de reconocimiento de voz; {e}")
