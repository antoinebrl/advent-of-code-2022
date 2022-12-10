import os
from itertools import accumulate


def parse(filename):
    # noops -> += [0]
    # addx X -> += [0, X]
    with open(filename) as f:
        return [int(x) if x.lstrip("-").isnumeric() else 0 for x in f.read().split()]

def run(add_values):
    return list(accumulate([1] + add_values))

def strength(signal):
    strength = sum([i * signal[i-1] for i in range(20, len(signal), 40)])
    return strength

def cdt(register_values):
    display = []
    for i in range(6):
        display.append([])
        for j in range(40):
            cycle = i * 40 + j
            x = register_values[cycle]
            display[i].append("#" if x - 1 <= j <= x + 1 else "." )
    return "\n".join(["".join(line) for line in display])


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    add_values = parse(input_file)
    register_values = run(add_values)

    solution1 = strength(register_values)
    print(f"part 1 - solution : {solution1}")

    solution2 = cdt(register_values)
    print(f"part 2 - solution :\n{solution2}")
