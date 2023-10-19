import speech_recognition as sr
import pyttsx3
import pywhatkit
import json
import urllib.request
import urllib.parse  



api_key = "api key"


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
        
    


    
'''Aca lo que hacemos es verificar que el usuario haya dicho 
Jarvis, reproduce. Si alguna de las dos falla no se escucha nada
'''


def run_yt():
    voice = alexa()

    # Reproducir algo en YouTube
    formas_reproducir = ["reproduci", "reproduce"]

    # Verificar si alguna forma está en la entrada de voz
    if any(forma in voice for forma in formas_reproducir):
        voice = voice.replace("reproduce", "reproduciendo")
        talk(voice)

        # Extraer el nombre de la canción
        song = voice
        for forma in formas_reproducir:
            song = song.replace(forma, "")
        pywhatkit.playonyt(song.strip())

    else:

       # Saber los subscriptores de un canal de YouTube
        formas_subs = ["cuantos Subs tiene", "cuantos subscriptores tiene", "subs de", "decime los subscriptores de"]

        if any(forma in voice for forma in formas_subs):
            canal_yt = voice

            #reemplaza la forma que tenemos para identificar que se quiere por blanco
            for forma in formas_subs:
                canal_yt = canal_yt.replace(forma, "")


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

run_yt()

