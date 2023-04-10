from typing import Union


def simple_calculator(num1: Union[float, int], num2: Union[float, int], operation: str) -> Union[float, int]:
    if operation == "/":
        return num1 / num2
    elif operation == "*":
        return num1 * num2
    elif operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
