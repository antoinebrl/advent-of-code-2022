import os
import re

def parse(filename):
    with open(filename) as f:
        return [[int(d) for d in re.findall("(\d+)", line)] for line in  f.readlines()]

def dist_l1(pt1, pt2):
    return abs(pt2[0] - pt1[0]) + abs(pt2[1] - pt1[1])

def coverage(sensors, row):
    ranges = []
    for (sx, sy), r in sensors.items():
        dx = r - abs(sy - row)  # horizontal distance to edge on a certain row
        if dx >= 0:
            ranges.append((sx - dx, sx + dx))
    return ranges

def find_hole(ranges):
    highest = 0
    for a, b in sorted(ranges):
        if a <= highest + 1:
            highest = max(highest, b)
        else:
            return a 
    return -1

def part1(sensors, row):
    ranges = coverage(sensors, row)
    # assuming no hole on the row
    a = min([a for a, b in ranges])
    b = max([b for a, b in ranges])
    return b - a

def part2(sensors, limit):
    for row in reversed(range(limit + 1)):
        ranges = coverage(sensors, row)
        col = find_hole(ranges)
        if col > 0:
            return col * 4_000_000 + row


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    signal = parse(input_file)
    sensors = {(sx, sy): dist_l1((sx, sy), (bx, by)) for sx, sy, bx, by in signal}

    solution1 = part1(sensors, row=2_000_000)
    print(f"part 1 - solution : {solution1}")

    solution2 = part2(sensors, limit=4_000_000)
    print(f"part 2 - solution : {solution2}")
