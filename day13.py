test_data = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

with open('input/day13.txt') as f:
    data = f.read()


def solve(data, part=1):
    points, folds = data.split('\n\n')
    points = [[int(coord) for coord in point.split(',')] for point in points.splitlines()]
    for fold in folds.splitlines():
        _, _, equation = fold.split()
        axis, n = equation.split('=')
        for point in points:
            coord = 0 if axis == 'x' else 1
            point[coord] = min(point[coord], 2*int(n) - point[coord])
        if part == 1:
            return len({(x, y) for x, y in points})
    height = max(y for x, y in points) + 1
    width = max(x for x, y in points) + 1
    grid = [['.' for _ in range(width)] for _ in range(height)] 
    for x, y in points:
        grid[y][x] = '#'
    return '\n'.join(''.join(row) for row in grid)


assert solve(test_data) == 17
print('Part 1:', solve(data))

assert solve(test_data, part=2) =="""#####
#...#
#...#
#...#
#####"""
print('Part 2:', solve(data, part=2), sep='\n')
