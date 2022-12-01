import os
import heapq

def main(topk=1):
    root_dir = os.path.dirname(__file__)
    with open(os.path.join(root_dir, "input.txt")) as f:
        data = f.read()
    calories = [sum(map(int, elf.split("\n"))) for elf in data.strip().split("\n\n")]
    return sum(heapq.nlargest(topk, calories))

if __name__ == "__main__":
    solution1 = main()
    print(f"part 1 - solution : {solution1}")

    solution2 = main(topk=3)
    print(f"part 2 - solution : {solution2}")
