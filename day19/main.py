import os
import re
from functools import cache, reduce, partial
import operator
import multiprocessing


def parse(filename):
    with open(filename) as f:
        return [list(map(int, re.findall(r'\d+', line))) for line in f.readlines()]

def solve(blueprint, duration):
    idx, ore_ore, clay_ore, obs_ore, obs_clay, goe_ore, geo_obs = blueprint
    max_ores = max(ore_ore, clay_ore, obs_ore, goe_ore)

    @cache
    def dfs(time, ore_robots=0, clay_robots=0, obs_robots=0, geodes_robots=0, ores=0, clays=0, obsidians=0, geodes=0):
        if time <= 0:
            return geodes
        
        max_geodes = 0

        if ores >= goe_ore and obsidians >= geo_obs:
            # Create geode robot
            g = dfs(time - 1,
                ore_robots, clay_robots, obs_robots, geodes_robots + 1,
                ores + ore_robots - goe_ore, clays + clay_robots, obsidians + obs_robots - geo_obs, geodes + geodes_robots
            )
            return max(max_geodes, g)
        
        g = dfs(time - 1,
            ore_robots, clay_robots, obs_robots, geodes_robots,
            ores + ore_robots, clays + clay_robots, obsidians + obs_robots , geodes + geodes_robots
        )
        max_geodes = max(max_geodes, g)

        if ores >= obs_ore and clays >= obs_clay:
            # Create obsidian robot
            g = dfs(time - 1,
                ore_robots, clay_robots, obs_robots + 1, geodes_robots,
                ores + ore_robots - obs_ore, clays + clay_robots - obs_clay, obsidians + obs_robots, geodes + geodes_robots
            )
            return max(max_geodes, g)
        if ores >= clay_ore:
            # Create clay robot
            g = dfs(time - 1,
                ore_robots, clay_robots + 1, obs_robots, geodes_robots,
                ores + ore_robots - clay_ore, clays + clay_robots, obsidians + obs_robots, geodes + geodes_robots
            )
            max_geodes = max(max_geodes, g)
        if ores >= ore_ore and ore_robots <= max_ores:
            # Create ore robot
            g = dfs(time - 1,
                ore_robots + 1, clay_robots, obs_robots, geodes_robots,
                ores + ore_robots - ore_ore, clays + clay_robots, obsidians + obs_robots, geodes + geodes_robots
            )
            max_geodes = max(max_geodes, g)

        return max_geodes

    return dfs(duration, ore_robots=1)

if __name__ == "__main__":
    input_file = os.path.join(os.path.dirname(__file__),  "input.txt")
    blueprints = parse(input_file)

    pool = multiprocessing.Pool(processes=8)
    geodes = pool.map(partial(solve, duration=24), blueprints)
    solution1 = sum([g * (i + 1) for i, g in enumerate(geodes)])
    print(f"part 1 - solution : {solution1}")
    
    # TODO: reduce search space
    geodes = pool.map(partial(solve, duration=32), blueprints[:3])
    solution2 = reduce(operator.mul, geodes, 1)
    print(f"part 2 - solution : {solution2}")
