import os


def parse(filename):
    with open(filename) as f:
        return f.readlines()

def dirdu(terminal):
    # Directory disk usage
    stack = []
    sizes = []

    def up():
        sizes.append(stack.pop(-1)) 
        if stack:
            stack[-1] += sizes[-1]

    def down():
        stack.append(0)

    def file(size):
        stack[-1] += size

    # We assume the input is a valid tree structure. Therefore names are irrelevant
    for line in terminal:
        match line.strip().split():
            case "$", "cd", "..":
                up()
            case "$", "cd", _:
                down()
            case "$", "ls":
                pass
            case "dir", _:
                pass
            case size, _:
                file(int(size))
    
    while stack:
        up()
    
    return sizes


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    terminal = parse(input_file)
    dir_sizes = dirdu(terminal)

    solution1 = sum(s for s in dir_sizes if s <= 100_000)
    print(f"part 1 - solution : {solution1}")

    solution2 = min(s for s in dir_sizes if s >= (max(dir_sizes) - 40_000_000))
    print(f"part 2 - solution : {solution2}")
