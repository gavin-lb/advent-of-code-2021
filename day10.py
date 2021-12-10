test_data = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

with open('input/day10.txt') as f:
    data = f.read()

def solve(data, part=1):
    pairs = {'(':')', '[':']', '{':'}', '<':'>'}
    corrupt_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    incomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}
    corrupt_total = 0
    incomplete = []
    for line in data.splitlines():
        opened = []
        for char in line:
            if char in pairs:
                opened.append(char)
            elif char != pairs[opened.pop()]:
                corrupt_total += corrupt_scores[char]
                break
        else:
            score = 0
            for char in reversed(opened):
                score = 5*score + incomplete_scores[pairs[char]]
            incomplete.append(score)
    
    if part == 1:
        return corrupt_total 
    else:
        incomplete.sort()
        return incomplete[len(incomplete)//2]

                
                
assert solve(test_data) == 26397
print('Part 1:', solve(data))

assert solve(test_data, part=2) == 288957
print('Part 2:', solve(data, part=2))
