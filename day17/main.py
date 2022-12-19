import os
from itertools import cycle


def parse(filename):
    with open(filename) as f:
        return cycle(list(f.readline().strip()))

def can_move_left(rock, stack):
    # No wall and no rock collision
    return not any(0b1000000 & line for line in rock) and not any((r << 1) & l for r, l in zip(rock, stack[-len(rock):]))

def can_move_right(rock, stack):
    # No wall and no rock collision
    return not any(0b0000001 & line for line in rock) and not any((r >> 1) & l for r, l in zip(rock, stack[-len(rock):]))

def move_one_step(command, rock, stack):
    if command == "<":
        if can_move_left(rock, stack):
            rock = [r << 1 for r in rock]
    else:
        if can_move_right(rock, stack):
            rock = [r >> 1 for r in rock]

    stopped = any(r & l for r, l in zip(rock, stack[-len(rock)-1:]))
    return rock, stopped

def drop_one_rock(commands, rock, stack):
    stack.extend([0b0000000] * (3 + len(rock)))
    top = len(stack)
    while True:
        command = next(commands)
        rock, stopped = move_one_step(command, rock, stack[:top])

        if stopped:
            break
        top -= 1
    
    for i, piece in enumerate(rock):
        stack[top - len(rock) + i] = piece | stack[top - len(rock) + i]

    while True:
        if stack[-1] == 0:
            stack.pop(-1)
        else:
            break
    return stack

def fall(commands, rocks, duration=2022):
    stack = [0b1111111] # simulate bottom
    for _ in range(duration):
        rock = next(rocks)
        stack = drop_one_rock(commands, rock, stack)
        # print("\n".join([f"{line:07b}" for line in reversed(stack)]), end="\n\n")
    return len(stack) - 1

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    commands = parse(input_file)

    rocks = cycle([
        [0b0011110],
        [0b0001000, 0b0011100, 0b0001000],
        [0b0011100, 0b0000100, 0b0000100],
        [0b0010000, 0b0010000, 0b0010000, 0b0010000],
        [0b0011000, 0b0011000]
    ])

    solution1 = fall(commands, rocks)
    print(f"part 1 - solution : {solution1}")

    duration_target = 1_000_000_000_000
    # values found manually by styding the occurence frequency of fully completed lines (0b1111111)
    cycle_duration = 1705
    cycle_height = 2649
    solution2 = fall(commands, rocks, duration=duration_target % cycle_duration) + (duration_target // cycle_duration) * cycle_height
    print(f"part 2 - solution : {solution2}")
