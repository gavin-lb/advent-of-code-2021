from re import findall
from collections import Counter


test_data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

with open('input/day14.txt') as f:
    data = f.read()


def solve(data, steps=10):
    template, pairs = data.split('\n\n')
    pairs = dict(findall('(\w\w) -> (\w)', pairs))
    count = Counter(map(''.join, zip(template, template[1:])))
    
    for _ in range(steps):
        for key, n in count.copy().items():
            count[key] -= n
            middle = pairs[key]
            first, second = key
            count[first + middle] += n
            count[middle + second] += n
            
    totals = Counter([template[0], template[-1]])
    for (first, second), n in count.items():
        totals[first] += n
        totals[second] += n
    (_, most), *_, (_, least) = totals.most_common()
    
    return (most - least)//2


assert solve(test_data) == 1588
print('Part 1:', solve(data))

assert solve(test_data, steps=40) == 2188189693529
print('Part 2:', solve(data, steps=40))
