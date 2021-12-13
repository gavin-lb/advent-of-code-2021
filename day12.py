import networkx as nx


test_data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

with open('input/day12.txt') as f:
    data = f.read()

def solve(data, double_visit=False):
    G = nx.Graph()
    for line in data.splitlines():
        G.add_edge(*line.split('-'))
    return sum(1 for _ in find_paths(G, double_visit=double_visit))

def find_paths(G, current_path=['start'], double_visit=False):
    current_node = current_path[-1]
    for node in G.neighbors(current_node):
        new_path = current_path + [node]
        if node == 'end':
            yield new_path
        elif node != 'start':
            if node.isupper() or node not in current_path:
                yield from find_paths(G, new_path, double_visit)
            elif double_visit:
                yield from find_paths(G, new_path, False)


assert solve(test_data) == 10
print('Part 1:', solve(data))

assert solve(test_data, double_visit=True) == 36
print('Part 2:', solve(data, double_visit=True))
