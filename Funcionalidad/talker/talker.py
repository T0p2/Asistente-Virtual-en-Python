import pyttsx3




#input: texto:str, #output: audio
def talk(text):
    voz = pyttsx3.init()

    #cambio de voces
    voices = voz.getProperty("voices")
    voz.setProperty("voice", voices[0].id)

    #velocidad 
    voz.setProperty('rate', 145)

    #para que hable
    voz.say(text)
    voz.runAndWait()

 