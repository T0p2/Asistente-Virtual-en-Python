import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser as web
import dotenv
import os



dotenv.load_dotenv()


#vars para spotify
client_id = os.getenv("ID_Spotify")
client_secret = os.getenv("Secret_Spotify")


def run_spo_music(author):

   
    author = author.replace("abriendo y buscando en spotify", "")
    
    author = author.replace(" ", "%20")

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


