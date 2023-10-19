import imaplib
import speech_recognition as sr
import pyttsx3
import pywhatkit
import json
import urllib.request
import urllib.parse 
import AVMYT as yt 



api_key = "AIzaSyCBfxe1t34R0ai0Xh_a9iCUKykDQ2x0ctc"

list = []
listener = sr.Recognizer() 
name = "Alexa"
voz = pyttsx3.init()

#cambio de voces
voices = voz.getProperty("voices")
voz.setProperty("voice", voices[0].id)


#input: texto:str, #output: audio
def talk(text):
    #para que hable
    voz.say (text)
    voz.runAndWait()





def alexa():

    voice = "Perdon no escuche"
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





def run_yt_video(song):

    song = song.replace("reproduciendo", "")
    pywhatkit.playonyt(song.strip())

    
def run_yt_sub(canal_yt):
        
    canal_yt = canal_yt.replace("buscando", "")
    # Hacemos una limpieza en el nombre del canal para que este sin espacios
    canal_yt = urllib.parse.quote(canal_yt)
    canal_yt = canal_yt.replace("%20", "")


    # Encontramos el canal de YouTube, nos devuelve un JSON, con ese JSON buscamos en statistics la cantidad de sub que tiene
    data = json.loads(urllib.request.urlopen(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={canal_yt.strip()}&key={api_key}').read().decode('utf-8'))
    
    #evaluamos si se encunetran resultados para el canal
    if data["pageInfo"]["totalResults"] == 0:
        talk("No se encontraron resultados para el canal.")
    else: 

    #agarramos del json el direccionario de items y extraemos los subs
        items = data.get('items', [])
        first_item = items[0]
        subs = first_item['statistics']['subscriberCount']



        # Imprimir la cantidad de suscriptores
        print(f"{canal_yt} tiene {subs} suscriptores.")
        talk(f"{canal_yt} tiene {subs} suscriptores.")




        

def call_functions():
    input = alexa()

# Reproducir algo en YouTube

    list = ["reproduci", "reproduce"]

 # Verificar si alguna forma está en la entrada de voz
    for forma in list:
        if forma in input:
                input = input.replace(forma, "reproduciendo")
                talk(input)

                run_yt_video(input)
    
    else:

    #Saber los subs de un canal
        list = ["cuantos Subs tiene", "cuantos subscriptores tiene", "Subs in youtube de ", "in Youtube"]


        for forma in list: 
            if forma in input:
                input = input.replace (forma,"buscando")
                talk(input)
                run_yt_sub(input)
        


        
            

    


call_functions()