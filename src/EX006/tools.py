from langchain.tools import BaseTool, tool


@tool
def multiply(a: float, b: float) -> float:
    """Multiply a * b and return the result

    Args:
        a: float multiplicand
        b: float mutiplier

    Return the resulting gloat of the equation a * b


    """

    return a * b


@tool
def sum(a: float, b: float) -> float:
    """sum a + b and return the result

    Args:
        a: float sum
        b: float sum

    Return the resulting gloat of the equation a + b


    """

    return a + b


@tool
def subtraction(a: float, b: float) -> float:
    """subtraction a - b and return the result

    Args:
        a: float sum
        b: float sum

    Return the resulting gloat of the equation a = b


    """

    return a - b


TOOLS: list[BaseTool] = [multiply, sum, subtraction]
TOOLS_BY_NAME: dict[str, BaseTool] = {tool.name: tool for tool in TOOLS}
