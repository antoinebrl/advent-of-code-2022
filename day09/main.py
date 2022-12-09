import os


def parse(filename):
    with open(filename) as f:
        return [[move, int(steps)] for move, steps in [line.split() for line in f.readlines()]]

def sign(x):
    return 1 if x >0 else 0 if x == 0 else -1

def visited_by_tail(moves, knots=1):
    rope = [[0, 0] for i in range(knots + 1)]
    visited = {(0, 0)}
    offsets = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}

    for direction, steps in moves:
        for _ in range(steps):
            head = rope[0]
            head[0] += offsets[direction][0]
            head[1] += offsets[direction][1]

            for i in range(len(rope) - 1):
                head, tail = rope[i], rope[i + 1]
                dist = (head[0] - tail[0])**2 + (head[1] - tail[1])**2
                if dist > 2:
                    tail[0] += sign(head[0] - tail[0])
                    tail[1] += sign(head[1] - tail[1])

            visited.add(tuple(rope[-1]))
    return visited

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    moves = parse(input_file)

    solution1 = len(visited_by_tail(moves))
    print(f"part 1 - solution : {solution1}")

    solution2 = len(visited_by_tail(moves, 9))
    print(f"part 2 - solution : {solution2}")
