import os
from collections import defaultdict
from itertools import product
from functools import cache


def parse(filename):
    valves = set()
    flow = {}
    distances = defaultdict(lambda: 100)
    with open(filename) as f:
        for line in f.readlines():
            valve = line[6:8]
            valves.add(valve)
            rate = int(line.split(";")[0].split("=")[-1])
            if rate > 0:
                flow[valve] = rate
            for next in line.split(";")[1].replace(",", "").split()[4:]:
                distances[valve, next] = 1 

    for k, i, j in product(valves, repeat=3):
        if k == i or k == j or i == j:
            continue
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    return  distances, flow

def search(total_time, distances, flow, elephant=False):
    @cache
    def dp(time, node, closed_valves, e=False):
        released_pressures = []
        for valve in closed_valves:
            remaining_time = time - distances[node, valve] - 1
            if remaining_time < 0:
                continue
            released_pressure = flow[valve] * remaining_time + dp(remaining_time, valve, closed_valves - {valve}, e)
            released_pressures.append(released_pressure)
        
        return max(released_pressures + [dp(total_time, "AA", closed_valves) if e else 0])
    return dp(total_time, node="AA", closed_valves=frozenset(flow.keys()), e=elephant)


if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    distances, flow = parse(input_file)

    solution1 = search(30, distances, flow)
    print(f"part 1 - solution : {solution1}")

    solution2 = search(26, distances, flow, elephant=True)
    print(f"part 2 - solution : {solution2}")
