import numpy as np
from scipy.signal import convolve2d


test_data = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

with open('input/day11.txt') as f:
    data = f.read()


def flash(arr):
    arr += np.ones(arr.shape, dtype=int)
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashed = np.zeros(arr.shape, dtype=bool)
    while arr.max() > 9:
        flashing = arr > 9
        flashed |= flashing
        arr += convolve2d(flashing.astype(int), mask, mode='same')
        arr[flashed] = 0
    return flashed

def part1(data, steps=100):
    arr = np.array([[*line] for line in data.splitlines()], dtype=int)
    return sum(flash(arr).sum() for _ in range(steps))

def part2(data):
    arr = np.array([[*line] for line in data.splitlines()], dtype=int)
    
    step = 0
    while np.any(arr):
        flash(arr)
        step += 1
    return step


assert part1(test_data) == 1656
print('Part 1:', part1(data))

assert part2(test_data) == 195
print('Part 2:', part2(data))
