import os

def sign(x):
    return 1 if x >0 else 0 if x == 0 else -1

def parse(filename):
    rocks = set()
    with open(filename) as f:
        for line in f.readlines():
            path = [tuple(map(int, edge.split(","))) for edge in line.split(" -> ")]
            for i in range(len(path) - 1):
                (x0, y0), (x1, y1) = path[i], path[i+1]
                while (x0, y0) != (x1, y1):
                    rocks.add((x0, y0))
                    x0 += sign(x1 - x0)
                    y0 += sign(y1 - y0)
                rocks.add((x0, y0))
    return rocks

def fall(pos, occupied, floor):
    x, y = pos
    for next in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if next not in occupied and next[1] != floor:
            return fall(next, occupied, floor)
    return (x, y)

def fill(rocks, void=True):
    sand = set()
    floor = max([y for x, y in rocks]) + 2

    while (500, 0) not in sand:
        x, y = fall((500, 0), rocks | sand, floor)
        if void and y == floor - 1:
            break
        sand.add((x, y))
    
    return len(sand)


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    rocks = parse(input_file)

    solution1 = fill(rocks)
    print(f"part 1 - solution : {solution1}")

    solution2 = fill(rocks, void=False)
    print(f"part 2 - solution : {solution2}")
