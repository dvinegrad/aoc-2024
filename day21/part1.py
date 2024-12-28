NUMS = {
    '0': (3, 1),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    'A': (3, 2),
    '': (3, 0)
}

ARROWS = {
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
    '': (0, 0)
}

DIR_TO_ARROW_MAP = {
    (-1, 0): '^',
    (1, 0): 'v',
    (0, -1): '<',
    (0, 1): '>'
}

def get_shortest(keys, sequence):
    path = []
    for i in range(len(sequence) - 1):
        cur, target = keys[sequence[i]], keys[sequence[i + 1]]
        next_path = []
        dirs = []
        
        for y in range(cur[1] - 1, target[1] - 1, -1):
            next_path.append((cur[0], y))
            dirs.append((0, -1))

        for x in range(cur[0] + 1, target[0] + 1):
            next_path.append((x, cur[1]))
            dirs.append((1, 0))

        for x in range(cur[0] - 1, target[0] - 1, -1):
            next_path.append((x, cur[1]))
            dirs.append((-1, 0))

        for y in range(cur[1] + 1, target[1] + 1):
            next_path.append((cur[0], y))
            dirs.append((0, 1))

        if keys[''] in next_path:
            dirs = list(reversed(dirs))

        path += [DIR_TO_ARROW_MAP[d] for d in dirs] + ['A']
    
    return "".join(path)

        
with open('input.txt') as f:
    lines = f.read().splitlines()

total_complexity = 0

for line in lines:
    l1 = get_shortest(NUMS, 'A' + line)
    l2 = get_shortest(ARROWS, 'A' + l1)
    l3 = get_shortest(ARROWS, 'A' + l2)

    total_complexity += int(line[0:-1]) * len(l3)

print(total_complexity)
