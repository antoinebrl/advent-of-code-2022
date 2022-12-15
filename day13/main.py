from functools import cmp_to_key
from itertools import zip_longest
import os

def parse(filename):
    with open(filename) as f:
        return [list(map(eval, lines.split("\n"))) for lines in f.read().split("\n\n")]

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return (a > b) - (a < b)
    if isinstance(a, int):
        a = [a]
    elif isinstance(b, int):
        b = [b]
    
    state = 0
    for u, v in zip_longest(a, b):
        if u is None:
            return -1
        if v is None:
            return 1
        
        state = compare(u, v)
        if state != 0:
            break
    return state

def part1(signals):
    indexes = [i + 1 for i, (a, b) in enumerate(signals) if compare(a, b) == -1]
    return sum(indexes)

def part2(signals):
    signals = [s for pair in signals for s in pair]
    dividers = [[[2]], [[6]]]
    signals.extend(dividers)
    signals = sorted(signals, key=cmp_to_key(compare))
    idx1 = signals.index(dividers[0]) + 1
    idx2 = signals.index(dividers[1]) + 1
    return idx1 * idx2


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    signals = parse(input_file)

    solution1 = part1(signals)
    print(f"part 1 - solution : {solution1}")

    solution2 = part2(signals)
    print(f"part 2 - solution : {solution2}")
