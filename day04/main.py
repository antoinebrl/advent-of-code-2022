import os

def parse(filename):
    with open(filename) as f:
        sections = [[list(map(int, elf.split("-"))) for elf in line.strip().split(",")] for line in f.readlines()]
    return sections

def is_contained(pair):
    union = [min(pair[0][0], pair[1][0]), max(pair[0][1], pair[1][1])]
    return union in pair

def is_overlapping(pair):
    sec1_starts_in_sec0 = pair[0][0] <= pair[1][0] <= pair[0][1]
    sec0_starts_in_sec1 = pair[1][0] <= pair[0][0] <= pair[1][1]
    return sec1_starts_in_sec0 or sec0_starts_in_sec1


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    sections = parse(input_file)

    solution1 = sum(map(is_contained, sections))
    print(f"part 1 - solution : {solution1}")

    solution2 = sum(map(is_overlapping, sections))
    print(f"part 2 - solution : {solution2}")
