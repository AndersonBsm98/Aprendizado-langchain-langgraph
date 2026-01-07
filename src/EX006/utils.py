from langchain.chat_models import BaseChatModel
from langchain_ollama import ChatOllama


def load_llm() -> BaseChatModel:
    return ChatOllama(model="llama3.2")
