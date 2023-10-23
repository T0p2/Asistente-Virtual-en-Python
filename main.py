from Funcionalidad.talker import talk
from Funcionalidad.listener import listen
from Funcionalidad.Metodos.YT import run_yt_video, run_yt_sub
from Funcionalidad.Metodos.Spotify import run_spo_music
import pyautogui
from time import sleep




        

def call_functions():

   
    input = listen()

    print(input)
    

# Reproducir algo en YouTube

    all_forms = ["reproducir en YouTube", "reproduce en YouTube"]

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
                    
                    talk("no etendi lo que dijiste")
                    call_functions()



if __name__ == '__main__':
    call_functions()

        
            

    


