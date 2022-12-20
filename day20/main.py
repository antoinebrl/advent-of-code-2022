import os


def parse(filename):
    with open(filename) as f:
        return list(map(int, f.readlines()))

def mixing(encrypted: list, key = 1, iterations = 1):
    n =  len(encrypted)
    indices = [i for i in range(n)]
    encrypted = [key * number  for number in encrypted]

    for _ in range(iterations):
        for i, number in enumerate(encrypted):
            old_idx = indices[i]
            new_idx = (old_idx + number) % (n - 1)
            
            shift = (old_idx > new_idx) - (old_idx < new_idx)
            for j in range(n):
                if min(old_idx, new_idx) <= indices[j] <= max(old_idx, new_idx):
                    indices[j] = (indices[j] + shift) % n
            indices[i] = new_idx
            assert sum(indices) == n * (n - 1) // 2

    zero_index = indices[encrypted.index(0)]
    return sum([encrypted[indices.index((zero_index + i) % n)] for i in [1_000, 2_000, 3_000]])


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    encrypted = parse(input_file)
    
    solution1 = mixing(encrypted)
    print(f"part 1 - solution : {solution1}")
    
    solution2 = mixing(encrypted, key=811589153, iterations=10)
    print(f"part 2 - solution : {solution2}")
