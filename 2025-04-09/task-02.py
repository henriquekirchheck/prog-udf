#!python

from random import randint
from typing import Literal


def execute(a: int, b: int, oper: Literal["sum", "sub", "mult"] = "sum")-> int:
    match oper:
        case "sum":
            return a + b
        case "sub":
            return a - b
        case "mult":
            return a * b

print(execute(randint(0, 100), randint(0, 100)))
