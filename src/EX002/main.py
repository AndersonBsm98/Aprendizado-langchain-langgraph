from langchain_ollama import ChatOllama
from rich import print

llm = ChatOllama(model="llama3.2", temperature=0.2)

response = llm.invoke("Explique odds implícitas em apostas esportivas")
print(response)
