from math import prod


test_data = """2199943210
3987894921
9856789892
8767896789
9899965678"""

with open('input/day9.txt') as f:
    data = f.read()

ADJACENT = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_basin(node, grid, valid_i, valid_j, basin):
    """
    Finds the basin using a stack-based flood fill algorithm.
    """

    basin.add(node)
    height, i, j = node
    for di, dj in ADJACENT:
        if i+di in valid_i and j+dj in valid_j:
            adjacent_height = grid[i+di][j+dj]
            adjacent_node = (adjacent_height, i+di, j+dj)
            if adjacent_node not in basin and height < adjacent_height < 9:
                find_basin(adjacent_node, grid, valid_i, valid_j, basin)
    return basin


def solve(data, part=1):
    grid = [list(map(int, row)) for row in data.splitlines()]
    valid_i = range(len(grid))
    valid_j = range(len(grid[0]))
    minima = [
        (height, i, j)
        for i, row in enumerate(grid)
        for j, height in enumerate(row)
        if height < min(
            grid[i+di][j+dj]
            for di, dj in ADJACENT
            if i+di in valid_i and j+dj in valid_j
        )
    ]
    if part == 1:
        return sum(height + 1 for height, i, j in minima)
    
    basins = [find_basin(minimum, grid, valid_i, valid_j, set()) for minimum in minima]
    basins.sort(key=len, reverse=True)
    return prod(map(len, basins[:3]))


assert solve(test_data) == 15
print('Part 1:', solve(data))

assert solve(test_data, part=2) == 1134
print('Part 2:', solve(data, part=2))
