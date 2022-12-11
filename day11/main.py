from dataclasses import dataclass
import math
import os


@dataclass
class Monkey:
    idx: int
    items: list[int]
    op: str
    test: str
    next: list[int, int]
    inspected: int = 0


def parse(filename):
    with open(filename) as f:
        blocks = f.read().split("\n\n")
    monkeys = []
    for block in blocks:
        lines = block.split("\n")
        idx = int(lines[0].split()[1][:-1])
        items = list(map(int, lines[1].split(":")[-1].split(",")))
        op = lines[2].split("=")[-1].replace("old", "item")
        test = int(lines[3].split()[-1])
        next = [int(lines[5].split()[-1]), int(lines[4].split()[-1])]
        monkeys.append(Monkey(idx, items, op, test, next))
    return monkeys

def keep_away(monkeys, turns=20, worried=False):
    lcm = 1 
    for m in monkeys:
        lcm = math.lcm(lcm, m.test)
    
    for i in range(turns):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspected += 1
                item = monkey.items.pop(0)
                item = eval(monkey.op)
                item = math.floor(item / 3) if not worried else item % lcm
                next = monkey.next[item % monkey.test == 0]
                monkeys[next].items.append(item)

def monkey_business(monkeys):
    most_active = sorted([m.inspected for m in monkeys])[-2:]
    return most_active[0] * most_active[1]


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")

    monkeys = parse(input_file)
    keep_away(monkeys, turns=20)
    solution1 = monkey_business(monkeys)
    print(f"part 1 - solution : {solution1}")

    monkeys = parse(input_file)
    keep_away(monkeys, turns=10_000, worried=True)
    solution2 = monkey_business(monkeys)
    print(f"part 2 - solution : {solution2}")
