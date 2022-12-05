from copy import deepcopy
import os


def parse(filename):
    ship, crates, moves = [], [], []
    with open(filename) as f:
        line = f.readline()
        while "[" in line:
            crates.append(line[1::4])
            line = f.readline()

        line = f.readline()
        while line := f.readline():
            moves.append(list(map(int, line.split()[1::2])))
        
    # Transpose line and column. Top crate is the first element of the list
    ship = list(zip(*crates))
    # Filter out empty crates
    ship = list(map(lambda x: list(filter(lambda c: c != " ", x)), ship))
    return ship, moves

def rearrange_1by1(ship, moves, bottom_to_top=False):
    for n, src, dst in moves:
        for i in range(n):
            idx = n - i - 1 if bottom_to_top else 0
            crate = ship[src - 1].pop(idx)
            ship[dst - 1].insert(0, crate)

def top_crates(ship):
    return "".join([stack.pop(0) for stack in ship])


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    ship, moves = parse(input_file)
    ship2 = deepcopy(ship)

    rearrange_1by1(ship, moves)
    solution1 = top_crates(ship)
    print(f"part 1 - solution : {solution1}")

    rearrange_1by1(ship2, moves, bottom_to_top=True)
    solution2 = top_crates(ship2)
    print(f"part 2 - solution : {solution2}")
