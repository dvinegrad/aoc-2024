import itertools

def get_lock(block):
    col_counts = [5] * 5
    for line in block[1:6]:
        for i in range(5):
            if line[i] == ".":
                col_counts[i] -= 1
    return col_counts

def get_key(block):
    col_counts = [0] * 5
    for line in block[1:6]:
        for i in range(5):
            if line[i] == "#":
                col_counts[i] += 1
    return col_counts


with open('input.txt') as f:
    lines = f.read().splitlines()

locks = []
keys = []

for i in range(0, len(lines), 8):
    block = lines[i:i+7]
    
    if block[0][0] == "#":
        locks.append(get_lock(block))

    elif block[0][0] == ".":
        keys.append(get_key(block))

ct_fit = sum([all([lock[i] + key[i] <= 5 for i in range(5)]) for lock, key in itertools.product(locks, keys)])

print(ct_fit)

