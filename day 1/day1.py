test_data = """199
200
208
210
200
207
240
269
260
263"""

with open('input.txt') as f:
    data = f.read()

def part1(data):
    *nums, = map(int, data.splitlines())
    return sum(a < b for a, b in zip(nums, nums[1:]))

def part2(data):
    *nums, = map(int, data.splitlines())
    size = 3
    window_sums = [sum(nums[i:i+size]) for i in range(len(nums)-size+1)]
    return sum(a < b for a, b in zip(window_sums, window_sums[1:]))


assert part1(test_data) == 7
print('Part 1:', part1(data))

assert part2(test_data) == 5
print('part 2:', part2(data))
