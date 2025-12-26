from typing import TypedDict

from langgraph.graph import StateGraph


class State(TypedDict):
    nodes_path: list[str]


# Definir os nodes
def node_a(state: State):
    pass


def node_b(state: State):
    pass


# Definir o Builder do grafo´
builder = StateGraph(State)

builder.add_node("A", node_a)
builder.add_node("B", node_b)

# conectar as edges

builder.add_edge("__start__", "A")
builder.add_edge("A", "B")
builder.add_edge("B", "__end__")


graph = builder.compile()

response = graph.invoke()
