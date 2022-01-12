import pyttsx3

robo = pyttsx3.init()

msg_robo = input('Escreva algo: ')

robo.say(msg_robo)

robo.runAndWait()