
import speech_recognition as sr
import pyttsx3
import pywhatkit
import json
import urllib.request
import urllib.parse 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser as web
import pyautogui
from time import sleep


#vars para spotify
client_id = "de9487ddcc674596a40a59c0dbca8013"
client_secret = "1b821bd750174cec8f757142155c3efc"



#vars para yt
api_key = "AIzaSyCBfxe1t34R0ai0Xh_a9iCUKykDQ2x0ctc"

#vars globales
all_forms = []
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





def alexa(voice):

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


def run_spo_music(author):

   
    author = author.replace("abriendo y buscando en spotify", "")
    
    

    if len(author) > 1:
    #Aca entramos a Spoify mediante nuestras credenciales y nos devuelve un json
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= client_id, client_secret=client_secret))
        result = sp.search(author)

        
        
    #nos devuelve todas las canciones que se encuntran
        for i in range(0, len(result["tracks"]["items"])):

                name_song = result["tracks"]["items"][i]["name"]

        #abrimos spotify
        web.open(result["tracks"]["items"][0]["uri"])
        sleep(5)
        #pyautogui.press("enter")



#esto es porque si no nos dan un autor pero si la cancion, buscamos la cancion
    else:

        talk("no escuche un autor en concreto")


        

def call_functions():

    sleep(2)
    input = alexa("hola soy Alexa, que queres hacer")

# Reproducir algo en YouTube

    all_forms = ["reproduci in youtube", "reproduce in youtube"]

 # Verificar si alguna forma está en la entrada de voz
    for forma in all_forms:
        if forma in input:
                input = input.replace(forma, "reproduciendo")
                talk(input)

                run_yt_video(input)
                break
    
    else:

    #Saber los subs de un canal
        all_forms = ["cuantos Subs tiene", "cuantos subscriptores tiene", "Subs in youtube de ", "in Youtube"]


        for forma in all_forms: 
            if forma in input:
                input = input.replace (forma,"buscando")
                talk(input)
                run_yt_sub(input)
                break

        else:
        
            all_forms = ["reproduci in Spotify","reproduce in Spotify", "busca in Spotify"]  
            
            for forma in all_forms:
                if forma in input:
                    input = input.replace(forma, "abriendo y buscando en spotify")
                    talk (input)

                    run_spo_music(input)
                else:
                    
                    if input == "hola soy Alexa, que queres hacer":
                        talk("Perdon no escuche nada")
                        
                        call_functions()
                    else:
                        talk("Perdon no entendi lo que dijiste")
                        
                        call_functions()





        
            

    


call_functions()