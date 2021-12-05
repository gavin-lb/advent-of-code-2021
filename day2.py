from collections import Counter


with open('input/day2.txt') as f:
    data = f.read()

test_data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def part1(data):
    count = Counter()
    for line in data.splitlines():
        instruction, n = line.split()
        count.update({instruction: int(n)})
    horizontal = count['forward']
    depth = count['down'] - count['up']
    return horizontal * depth

def part2(data):
    horizontal = depth = aim = 0
    for line in data.splitlines():
        instruction, n = line.split()
        n = int(n)
        if instruction == 'forward':
            horizontal += n
            depth += aim * n
        elif instruction == 'up':
            aim -= n
        elif instruction == 'down':
            aim += n
    return horizontal * depth


assert part1(test_data) == 150
print('Part 1:', part1(data))

assert part2(test_data) == 900
print('Part 2:', part2(data))
