from langchain_core.messages import HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
from rich import print

llm = ChatOllama(model="llama3.2", temperature=0.2)

system_message = SystemMessage(
    "Voce e um analista futebolisco que entende tudo sobre futebol "
    "Nesse momento voce terá que dar dados estatisticos comprovando seus pontos"
)
human_message = HumanMessage('"Manchester United ainda e maior que o liverpool? "')
messages = [system_message, human_message]


response = llm.invoke(messages)
print(response)
