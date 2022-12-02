import os

def rps_parse():
    # A = X = Rock = 0
    # B = Y = Paper = 1
    # C = Z = Scissors = 2
    root_dir = os.path.dirname(__file__)
    with open(os.path.join(root_dir, "input.txt")) as f:
        moves = []
        for line in f.readlines():
            shape1, shape2 = line.split()
            moves += [[ord(shape1) - ord('A'), ord(shape2) - ord('X')]]
    return moves

def score1(moves):
    score = 0
    for m1, m2 in moves:
        score += m2 + 1  # shape
        score += (m2 - m1 + 1) % 3 * 3  # game result
    return score

def score2(moves):
    score = 0
    for m1, m2 in moves:
        score += m2 * 3  # game results
        score += (m1 + m2 - 1) % 3 + 1  # shape
    return score
    

if __name__ == "__main__":
    moves = rps_parse()

    solution1 = score1(moves)
    print(f"part 1 - solution : {solution1}")

    solution2 = score2(moves)
    print(f"part 2 - solution : {solution2}")
