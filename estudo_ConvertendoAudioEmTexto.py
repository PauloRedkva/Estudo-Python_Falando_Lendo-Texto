# pip install SpeechRecognition
# pip install pipwin
# pipwin install pyaudio

import speech_recognition as sr

def reconhecer_fala():
    # Habilita o microfone
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        # Reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        print("Fale algo, por favor: ")
        # guarda o audio falado na variavel 'audio', o audio é finalizado nas pausas grandes
        audio = microfone.listen(source)
        try:
            # audio sera interpretado na lingua portuguesa
            frase = microfone.recognize_google(audio, language='pt-BR')
            print("Você disse: " + frase)
        except:
            print("Não entendi o que você disse!")
        return frase

reconhecer_fala()
