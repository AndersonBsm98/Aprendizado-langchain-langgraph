from collections.abc import Sequence
from typing import Annotated, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, START, StateGraph, add_messages
from rich import print
from rich.markdown import Markdown

llm = ChatOllama(model="llama3.2")


class AgentState(TypedDict):  # Defino o meu state
    messages: Annotated[Sequence[BaseMessage], add_messages]


def call_llm(state: AgentState):  # Defino o node
    llm_result = llm.invoke(state["messages"])
    # llm_result = AIMessage("Oi como vai?")
    return {"messages": [llm_result]}


# crio o StateGraph

builder = StateGraph(
    AgentState, context_schema=None, input_schema=AgentState, output_schema=AgentState
)


# Adicionar nodes ao Grapho

builder.add_node("call_llm", call_llm)
builder.add_edge(START, "call_llm")
builder.add_edge("call_llm", END)


# Compilar o grafo


graph = builder.compile()

if __name__ == "__main__":
    current_message: Sequence[BaseMessage] = []
    while True:
        user_input = input("Digite sua mensagem: ")
        print(Markdown("---"))

        if user_input.lower() in ["q", "quit"]:
            print("Prepara o BYD e tchau")
            print(Markdown("---"))
            break

        human_message = HumanMessage(user_input)
        current_message = [*current_message, human_message]
        result = graph.invoke({"messages": current_message})
        current_message = result["messages"]
        print(Markdown(str(result["messages"][-1].content)))
        print(Markdown("---"))
