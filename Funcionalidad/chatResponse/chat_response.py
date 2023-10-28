from Funcionalidad.talker.talker import talk
from Funcionalidad.listen.listener import listen
from Funcionalidad.langchain.langchain_brain import LangChainBrainAssistant



''' Aca lo que vamos a hacer es hacer lo intermedio entre
nuestra query a traves de la voz y la respuesta atreves de chat gpt
utilizando las librerias que creamos 'langchain' , 'lsiten' y 'talker' 
'''

langchain_assistant = LangChainBrainAssistant()


def welcome ():
    talk(
        'Hola, bienvenido hazme cualquier pregunta sobre'
        'cualquier cosa'
    )

def listen_for_response():
    return listen()

def generate_response():
    welcome()
    response = langchain_assistant.chat_func(listen_for_response())
    print(response)
    talk(response)

