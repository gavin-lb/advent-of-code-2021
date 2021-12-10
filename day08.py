from itertools import groupby

test_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

with open('input/day8.txt') as f:
    data = f.read()

def part1(data):
    output_lens = []
    for line in data.splitlines():
        digits, output = line.split(' | ')
        *lens, = map(len, output.split())
        output_lens.extend(lens)
    return sum(output_lens.count(i) for i in [2, 3, 4, 7])

def part2(data):
    total = 0
    for line in data.splitlines():
        digits, output = line.split(' | ')
        digits = sorted(digits.split(), key=len)
        len_dict = {k: [set(d) for d in g] for k, g in groupby(digits, key=len)}
        digit_dict = {k: len_dict[v][0] for k, v in [(1, 2), (4, 4), (7, 3), (8, 7)]}
        
        # Using the following labels for display segments:
        #  a a a
        # b     c
        # b     c
        # b     c
        #  d d d 
        # e     f
        # e     f
        # e     f
        #  g g g

        # since 0, 6, 9 all have 6 segments, their intersection gives us segments a, b, f, g
        abfg = set.intersection(*len_dict[6])
        # 8 has all segments, so we can find the inverse by taking the difference with 8
        cde = digit_dict[8] - abfg
        # 4 has segments b, c, d, f, so we can find e by:
        e = cde - digit_dict[4]
        digit_dict[9] = digit_dict[8] - e
        d = digit_dict[9] - abfg - digit_dict[1]
        c = cde - d - e
        digit_dict[6] = digit_dict[8] - c
        digit_dict[0] = digit_dict[8] - d
        digit_dict[5] = digit_dict[6] - e
        b = digit_dict[4] - digit_dict[1] - d
        digit_dict[3] = digit_dict[9] - b
        f = digit_dict[1] - c
        digit_dict[2] = digit_dict[3] - f | e
        
        segment_dict = {frozenset(v): str(k) for k, v in digit_dict.items()}
        output_num = ''.join(segment_dict[frozenset(num)] for num in output.split())
        total += int(output_num)
    return total

assert part1(test_data) == 26
print('Part 1:', part1(data))

assert part2(test_data) == 61229
print('Part 2:', part2(data))
