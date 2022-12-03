import os
import itertools


def parse(file):
    with open(file) as f:
        return f.read().splitlines()

def gen1(rucksacks):
    # Split bags into two compartments 
    for rucksack in rucksacks:
        n = len(rucksack)//2
        compartments = set(rucksack[:n]), set(rucksack[n:])
        yield compartments

def gen2(rucksacks):
    # Group rucksacks by 3
    rucksacks = iter(rucksacks)
    while group := list(itertools.islice(rucksacks, 3)):
        bags = map(set, group)
        yield bags

def find_duplicates(sets):
    # Assuming there is only one element in the intersection
    return set.intersection(*sets).pop()

def priority(item):
    # a..z = 1..26 and A..Z = 27..52
    return ord(item) - (96 if item.islower() else 38)

def total_score(items):
    return sum(map(priority, items))
    

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__), "input.txt")
    rucksacks = parse(input_file)

    solution1 = total_score(map(find_duplicates, gen1(rucksacks)))
    print(f"part 1 - solution : {solution1}")

    solution2 = total_score(map(find_duplicates, gen2(rucksacks)))
    print(f"part 2 - solution : {solution2}")
