import pywhatkit
import json
import urllib.request
import urllib.parse 
import dotenv
import os



dotenv.load_dotenv()

api_key_yt = os.getenv("API_YT")


def run_yt_video(song):

    song = song.replace("reproduciendo", "")
    pywhatkit.playonyt(song.strip())



    
def run_yt_sub(canal_yt):
        
    canal_yt = canal_yt.replace("buscando", "")
    # Hacemos una limpieza en el nombre del canal para que este sin espacios
    canal_yt = urllib.parse.quote(canal_yt)
    canal_yt = canal_yt.replace("%20", "")


    # Encontramos el canal de YouTube, nos devuelve un JSON, con ese JSON buscamos en statistics la cantidad de sub que tiene
    data = json.loads(urllib.request.urlopen(f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={canal_yt.strip()}&key={api_key_yt}').read().decode('utf-8'))
    
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

