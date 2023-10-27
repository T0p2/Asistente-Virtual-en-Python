from Funcionalidad.talker.talker import talk
from Funcionalidad.listen.listener import listen
from Funcionalidad.langchain.langchain_brain import chat



''' Aca lo que vamos a hacer es hacer lo intermedio entre
nuestra query a traves de la voz y la respuesta atreves de chat gpt
utilizando las librerias que creamos 'langchain' , 'lsiten' y 'talker' 
'''

def welcome ():
    talk(
        'Hola, bienvenido hazme cualquier pregunta sobre'
        'cualquier cosa'
    )

def listen_for_response():
    return listen()

def generate_response():
    welcome()
    response = chat(listen_for_response())
    print(response)
    talk(response)

