from Funcionalidades.talker import talk
from Funcionalidades.listener import listen
from Funcionalidades.Metodos.YT import run_yt_video, run_yt_sub
from Funcionalidades.Metodos.Spotify import run_spo_music
import pyautogui
from time import sleep




        

def call_functions():

    sleep(2)
    input = listen()

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




if __name__ == '__main__':
    call_functions()

        
            

    


