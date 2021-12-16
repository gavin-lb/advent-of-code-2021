import numpy as np
from heapq import heappop, heappush
from time import perf_counter

test_data = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

with open('input/day15.txt') as f:
    data = f.read()


def solve(data):
    """
    Finds the path to exit with minimum total risk using an A* search with
    best-case heuristic being all 1s to the exit. 
    """
    
    risks = np.array([list(row) for row in data.splitlines()], dtype=int)
    totals = np.full(risks.shape, np.inf)
    totals[0, 0] = 0
    visited = np.zeros(risks.shape, dtype=bool)
    heuristics = np.flip(np.indices(risks.shape).sum(axis=0))
    heap = [(heuristics[0, 0], (0, 0))]
    max_x, max_y = totals.shape
    
    while heap and np.isinf(totals[-1, -1]):
        heuristic, (x, y) = heappop(heap)
        total = totals[x, y]
        if not visited[x, y]:
            visited[x, y] = True
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                if 0 <= x+dx < max_x and 0 <= y+dy < max_y:
                    new_total = total + risks[x+dx, y+dy]
                    if new_total < totals[x+dx, y+dy]:
                        totals[x+dx, y+dy] = new_total
                        heappush(heap, (new_total + heuristics[x+dx, y+dy], (x+dx, y+dy)))
    return int(totals[-1, -1])

def expand(data, mult=5):
    risks = np.array([list(row) for row in data.splitlines()], dtype=int)
    for axis in 0, 1:
        risks = np.concatenate([risks + i for i in range(mult)], axis=axis)
    risks = (risks - 1) % 9 + 1
    return '\n'.join(''.join(row) for row in risks.astype(str))
    

assert solve(test_data) == 40
start = perf_counter()
print(f'Part 1: {solve(data)} (in {perf_counter() - start:.2f} seconds)')

assert solve(expand(test_data)) == 315
start = perf_counter()
print(f'Part 2: {solve(expand(data))} (in {perf_counter() - start:.2f} seconds)')
