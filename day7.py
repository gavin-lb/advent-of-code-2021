from collections import Counter

test_data = '16,1,2,0,4,2,7,1,2,14'

with open('input/day7.txt') as f:
    data = f.read()

def min_trough(nums):
    """
    Finds by binary search the minimum of a trough sequence, that is, one that is
    monotonically decreasing until a minima and thereafter monotonically increasing.
    Time complexity: O(log(n)). 
    """
    n = len(nums)
    if n == 1:
        return nums[0]
    mid = n // 2
    return min_trough(nums[:mid] if nums[mid - 1] < nums[mid] else nums[mid:])


def solve(data, part=1):
    count = Counter(map(int, data.split(',')))
    sequence = [
        sum(
            # for part 2 using \sum_{k=1}^n k = n(n+1)/2
            v * (abs(k-i) if part == 1 else abs(k-i) * (abs(k-i)+1) // 2)
            for k, v in count.items()
        )
        for i in range(1, max(count) + 1)
    ]
    return min_trough(sequence)
 

assert solve(test_data) == 37
print('Part 1:', solve(data))

assert solve(test_data, part=2) == 168
print('Part 2:', solve(data, part=2))
