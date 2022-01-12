# pip instal pyttsx3
import pyttsx3
# Colocar o texto arquivo .txt
f = open('F:/ZenPython/zen.txt','r', encoding="utf8")
texto = f.read()
# inicia serviço biblioteca
speaker = pyttsx3.init()
# metodo de voz
voices = speaker.getProperty('voices')
# ver as vozes instaladas na maquina
for voice in voices:
    # traz os idiomas de voz instalados em sua maquina
    print(voice, voice.id)
# define a voz padrao, no meu caso o portugues era o[0] (iniciando do zero)
speaker.setProperty('voice', voices[0].id)
rate = speaker.getProperty('rate')
# muda velocidade da leitura, quando menor mais lento
speaker.setProperty('rate', rate - 25)
# escreve o texto na tela
print(texto)
# define o texto que será lido
speaker.say(texto)
# le o texto
speaker.runAndWait()
# fecha o modo deleitura do arquivo txt
f.close()
