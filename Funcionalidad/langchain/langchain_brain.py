import dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
#from modules.roles_templates.roles_templates import roles_templates
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

from Funcionalidad.templates.template import brain_template


dotenv.load_dotenv()

#creamos la variable chat con una temperatura que es cuanto preciso es
chat_ia = ChatOpenAI(temperature = 0.3)


class LangChainBrainAssistant:
    def chat_func(self, text):
    #esto para asignarle el rol que cumple el chat
        assistant_prompt = SystemMessagePromptTemplate.from_template(brain_template)

    #esto para mandarle nuestro mensaje
        user_prompt = HumanMessagePromptTemplate.from_template("{text}")

    #le pasamos los promt
        chat_promt = ChatPromptTemplate.from_messages(
            [assistant_prompt, user_prompt]
        )

    #respuest de chat gpt, atraves de nuestra peticion
        answer = chat_ia(chat_promt.format_prompt(text = text).to_messages())

        return answer

