test_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

with open('input.txt') as f:
    data = f.read()

def part1(data):
    nums = data.splitlines()
    bit_length = len(nums[0])
    gamma_bin = ''.join('0' if bits.count('0') > len(nums)/2 else '1' for bits in zip(*nums))
    gamma = int(gamma_bin, 2)
    epsilon = (1 << bit_length) - 1 ^ gamma   # ones' complement
    return gamma * epsilon

def partition(nums, index):
    d = {'0':[], '1':[]}
    for num in nums:
        d[num[index]].append(num)
    return sorted(d.values(), key=len)

def part2(data):
    nums = data.splitlines()
    bit_length = len(nums[0])
    majority = minority = nums
    for index in range(bit_length):
        _, majority = partition(majority, index)
        minority, _ = partition(minority, index)
        if len(majority) == 1:
            oxygen, = majority
        if len(minority) == 1:
            co2, = minority
    return int(oxygen, 2) * int(co2, 2)

    
assert part1(test_data) == 198
print('Part 1:', part1(data))

assert part2(test_data) == 230
print('Part 2:', part2(data))
