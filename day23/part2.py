from collections import defaultdict
import itertools

def is_clique(connections, nodes):
    for i, node1 in enumerate(nodes):
        for _, node2 in enumerate(nodes[i+1:]):
            if node2 not in connections[node1]:
                return False

    return True

def max_clique_starting_at(connections, node):
    neighbors = connections[node]
    for i in range(len(neighbors), 1, -1):
        for group in itertools.combinations(neighbors, i):
            if is_clique(connections, group):
                return set([node, *group])

    return set()


with open('input.txt') as f:
    lines = f.read().splitlines()
    
connections = defaultdict(set)
pairs = [tuple(line.split("-")) for line in lines]
for pair in pairs:
    connections[pair[0]].add(pair[1])
    connections[pair[1]].add(pair[0])

cliques = [max_clique_starting_at(connections,  node) for node in connections.keys()]
max_clique = max(cliques, key=len)

print(",".join(sorted(max_clique)))