import os
import numpy as np


def parse(filename):
    with open(filename) as f:
        elevataion =  np.asarray([[ord(c) - ord('a') for c in line.strip()] for line in f.readlines()])
    start = tuple([x[0] for x in np.where(elevataion == ord('S') - ord('a'))])  # np.array is not hashable
    end = tuple([x[0] for x in np.where(elevataion == ord('E') - ord('a'))])  # np.array is not hashable
    elevataion[start] = 0
    elevataion[end] = 25
    return elevataion, start, end

def connected_neighbors(point, shape):
    neighbors = [(point[0] + dy, point[1] + dx) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]]
    neighbors = [n for n in neighbors if 0 <= n[0] < shape[0] and 0 <= n[1] < shape[1]]
    return neighbors

def part1_neighbors(elevation, point):
    neighbors = [n for n in connected_neighbors(point, elevation.shape) if elevation[n] - elevation[point] <= 1]
    return neighbors

def part2_neighbors(elevation, point):
    neighbors = [n for n in connected_neighbors(point, elevation.shape) if elevation[point] - elevation[n] <= 1]
    return neighbors

def bfs(elevation, start, step_fn, is_end_fn):
    visited = set()
    to_visit = [(0, start)]

    while to_visit:
        steps, current = to_visit.pop(0)

        if is_end_fn(current):
            return steps
        if current in visited:
            continue
        visited.add(current)

        for next in step_fn(elevation, current):
            to_visit.append((steps + 1, next))


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    elevation, start, end = parse(input_file)

    solution1 = bfs(elevation, start, part1_neighbors, lambda x: x == end)
    print(f"part 1 - solution : {solution1}")

    solution2 = bfs(elevation, end, part2_neighbors, lambda x: elevation[x] == 0)
    print(f"part 2 - solution : {solution2}")
