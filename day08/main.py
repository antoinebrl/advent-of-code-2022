import os


def parse(filename):
    with open(filename) as f:
        return [list(map(int, line.strip())) for line in f.readlines()]

def visible_trees(plantation):
    visible = 0
    for i in range(len(plantation)):
        for j in range(len(plantation[0])):
            tree = plantation[i][j]
            left = plantation[i][:j]
            right = plantation[i][j+1:]
            top = [plantation[k][j] for k in range(i)]
            bottom = [plantation[k][j] for k in range(i+1, len(plantation))]
            
            if (
                tree > max(left, default=-1)
                or tree > max(right, default=-1)
                or tree > max(top, default=-1)
                or tree > max(bottom, default=-1)
            ):
                visible += 1
    return visible

def scenic_score(plantation):
    best_score = 0
    n = len(plantation)
    m = len(plantation[0])
   
    for i in range(n):
        for j in range(m):
            score = 1
            tree = plantation[i][j]

            for dx, dy in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                x, y = i + dx, j + dy
                while 0 <= x < n and 0 <= y < m:
                    if plantation[x][y] >= tree:
                        break
                    x += dx
                    y += dy
                else:
                    # One tree too far
                    x -= dx
                    y -= dy
                score *= abs(i - x) + abs(j - y)

            if score > best_score:
                best_score = score
    
    return best_score


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    plantation = parse(input_file)

    solution1 = visible_trees(plantation)
    print(f"part 1 - solution : {solution1}")

    solution2 = scenic_score(plantation)
    print(f"part 2 - solution : {solution2}")
