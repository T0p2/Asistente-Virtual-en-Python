
import speech_recognition as sr
import pywhatkit

listener = sr.Recognizer() 
name = "Alexa"




def listen(voice):
    talk(voice)

    #codigo para que nos escuche
    with sr.Microphone() as source:
        print('Deci algo ')
        audio = listener.listen(source)
    
        try:
            
            voice = listener.recognize_google(audio)

            print('Dijiste: {}'.format(voice))

            

    #si la maquina escucha su nombre en el audio, responde.
            if(name in voice):
                voice = voice.replace(name, "")

        
        except:
            print('Sorry could not hear')
            
    return(voice)
    

