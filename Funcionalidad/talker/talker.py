import pyttsx3


voz = pyttsx3.init()

#cambio de voces
voices = voz.getProperty("voices")
voz.setProperty("voice", voices[0].id)

#input: texto:str, #output: audio
def talk(text):
    #para que hable
    voz.say (text)
    voz.runAndWait()

 