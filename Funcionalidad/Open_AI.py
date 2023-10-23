import dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (

    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

from template.template import brain_template

dotenv.load_dotenv()

chat = ChatOpenAI(temperature=0.2)

class LangChainBrainAssistant:
    def chat(self, user_text):
        assistant_prompt = SystemMessagePromptTemplate.from_template(brain_template)
        user_prompt = HumanMessagePromptTemplate.from_template("{input}")
        chat_promt = ChatPromptTemplate.from_messages(
            [assistant_prompt, user_promt]
        )

        response = chat(chat_prompt.format_prompt(user_text=user_text).to_messages())
        return response