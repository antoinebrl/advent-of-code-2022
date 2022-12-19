import os
import numpy as np


def parse(filename):
    with open(filename) as f:
        return [tuple(map(int, line.split(","))) for line in f.readlines()]

def part1(scan):
    lava = np.zeros(np.max(scan, axis=0) + 1, dtype=bool)

    for drop in scan:
        lava[drop] = 1

    exposed_faces = 0
    for i in range(lava.shape[0]):
        for j in range(lava.shape[1]):
            for k in range(lava.shape[2]):
                if not lava[i, j, k]:
                    continue
                for d in [-1, 1]:
                    exposed_faces += not lava[i + d, j, k] if 0 <= i + d < lava.shape[0] else 1
                    exposed_faces += not lava[i, j + d, k] if 0 <= j + d < lava.shape[1] else 1
                    exposed_faces += not lava[i, j, k + d] if 0 <= k + d < lava.shape[2] else 1
    return exposed_faces

def get_adjacents(point, limits):
    for d in [-1, 1]:
        if 0 <= point[0] + d < limits[0]:
            yield point[0] + d, point[1], point[2]
        if 0 <= point[1] + d < limits[1]:
            yield point[0], point[1] + d, point[2]
        if 0 <= point[2] + d < limits[2]:
            yield point[0], point[1], point[2] + d
        
def part2(scan):
    size = np.max(scan, axis=0)
    to_visit = set([drop for drop in scan if np.any(0 == drop) or np.any(size == drop)])
    visited = set()
    exposed_faces = 0

    while to_visit:
        current = to_visit.pop()
        visited.add(current)

        for adjacent in get_adjacents(current, size):
            if adjacent in scan:
                exposed_faces += 1
            elif adjacent not in visited:
                to_visit.add(adjacent)

    return exposed_faces


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    scan = parse(input_file)
    
    solution1 = part1(scan)
    print(f"part 1 - solution : {solution1}")

    solution2 = part2(scan)
    print(f"part 2 - solution : {solution2}")
