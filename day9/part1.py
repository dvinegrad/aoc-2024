with open('input.txt') as f:
    disk_map = [int(c) for c in f.read()]

blocks = []

file_id = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        blocks += [file_id] * disk_map[i]
        file_id += 1
    else:
        blocks += ['.'] * disk_map[i]

empty_blocks = []
for i in range(len(blocks)):
    if blocks[i] == '.':
        empty_blocks += [i]

idx = len(blocks) - 1
while idx > empty_blocks[0]:
    if blocks[idx] != '.':
        first_empty_idx = empty_blocks.pop(0)
        blocks[first_empty_idx] = blocks[idx]
        blocks[idx] = '.'
    idx -= 1

checksum = 0

for i in range(len(blocks)):
    if blocks[i] != '.':
        checksum += i * blocks[i]

print(checksum)