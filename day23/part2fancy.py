from collections import defaultdict

def bron_kerbosch(connections, R, P, X):
    if len(P) == 0 and len(X) == 0:
        yield R

    while len(P) > 0:
        v = P.pop()
        yield from bron_kerbosch(connections, R.union(set([v])), P.intersection(connections[v]), X.intersection(connections[v]))
        X = X.union(set([v]))


with open('input.txt') as f:
    lines = f.read().splitlines()
    
connections = defaultdict(set)
pairs = [tuple(line.split("-")) for line in lines]
for pair in pairs:
    connections[pair[0]].add(pair[1])
    connections[pair[1]].add(pair[0])

cliques = bron_kerbosch(connections, set(), set(connections.keys()), set())

print(",".join(sorted(max(cliques, key=len))))