from collections import Counter, deque

test_data = "3,4,3,1,2"

with open('input/day6.txt') as f:
    data = f.read()

def solve(data, days=80):
    *nums, = map(int, data.split(','))
    count = Counter(nums)
    fish = deque(count[day] for day in range(9))
    for _ in range(days):
        fish.rotate(-1)
        fish[6] += fish[-1]
    return sum(fish)

assert solve(test_data) == 5934
print('Part 1:', solve(data))

assert solve(test_data, days=256) == 26984457539
print('Part 2:', solve(data, days=256))
