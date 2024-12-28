from collections import defaultdict

with open('input.txt') as f:
    lines = f.read().splitlines()
    
connections = defaultdict(set)
pairs = [tuple(line.split("-")) for line in lines]
for pair in pairs:
    connections[pair[0]].add(pair[1])
    connections[pair[1]].add(pair[0])

trios = set()
for pair in pairs:
    intersection = connections[pair[0]].intersection(connections[pair[1]])
    for val in intersection:
        trios.add(tuple(sorted((pair[0], pair[1], val))))

trios_with_t = [trio for trio in trios if any(v.startswith("t") for v in trio)]
print(len(trios_with_t))