import os
import re
from fractions import Fraction as F


def parse(filename):
    with open(filename) as f:
        return {line[:4]: line.strip()[6:] for line in  f.readlines()}

def compute(expression, ops):
    while groups := re.findall('[a-z]+', expression):
        for name in groups:
            expression = expression.replace(name, "F(" + ops[name] + ")")
    return eval(expression)

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    ops = parse(input_file)

    solution1 = compute(ops["root"], ops)
    print(f"part 1 - solution : {solution1}")
    
    # We can find the solution of the linear equation ax+b=0 by computing
    # a and b after evaluating the function for two different values x0 and x1
    ops["root"] = ops["root"].replace("+", "-")
    
    ops["humn"] = "0"
    f0 = compute(ops["root"], ops)
    ops["humn"] = "10"
    f1 = compute(ops["root"], ops)

    a = (f1 - f0) / eval(ops["humn"])
    b = f0
    solution2 = - b / a
    print(f"part 2 - solution : {solution2}")

    # Using sympy to solve the equation
    from sympy import solve, symbols

    expression = ops["root"] = ops["root"].replace("+", "-")
    ops["humn"] = "X"
    X = symbols("X")

    while groups := re.findall('[a-z]+', expression):
        for name in groups:
            expression = expression.replace(name, "(" + ops[name] + ")")

    solution2 = solve(expression)[0]
    print(f"part 2 - solution : {solution2}")
