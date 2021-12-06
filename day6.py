from collections import Counter

test_data = "3,4,3,1,2"

with open('input/day6.txt') as f:
    data = f.read()

def solve(data, days=80):
    *nums, = map(int, data.split(','))
    fish = Counter(nums)
    for _ in range(days):
        fish = {k-1: v for k, v in fish.items()}
        if -1 in fish:
            new_fish = fish.pop(-1)
            fish[6] = fish.get(6, 0) + new_fish
            fish[8] = fish.get(8, 0) + new_fish
    return sum(fish.values())

assert solve(test_data) == 5934
print('Part 1:', solve(data))

assert solve(test_data, days=256) == 26984457539
print('Part 2:', solve(data, days=256))
