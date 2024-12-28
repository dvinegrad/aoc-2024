with open('input.txt') as f:
    disk_map = [int(c) for c in f.read()]

blocks = []
empty_blocks = {}

file_id = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        blocks += [file_id] * disk_map[i]
        file_id += 1
    elif disk_map[i] > 0:
        empty_blocks[len(blocks)] = disk_map[i]
        blocks += ['.'] * disk_map[i]

empty_block_starts = sorted(empty_blocks.keys())

idx = len(blocks) - 1
while idx > empty_block_starts[0]:
    if blocks[idx] != '.':
        file_id = blocks[idx]
        file_len = 0
        while blocks[idx] == file_id:
            file_len += 1
            idx -= 1
        
        for i in range(len(empty_block_starts)):
            empty_start = empty_block_starts[i]
            empty_block_len = empty_blocks[empty_start]
            if empty_start > idx:
                break

            if empty_block_len >= file_len:
                for n in range(idx + 1, idx + 1 + file_len):
                    blocks[n] = '.'

                for n in range(empty_start, empty_start + file_len):
                    blocks[n] = file_id

                if empty_block_len == file_len:
                    del empty_blocks[empty_start]
                    empty_block_starts.pop(i)
                else:
                    empty_block_starts[i] += file_len
                    del empty_blocks[empty_start]
                    empty_blocks[empty_start + file_len] = empty_block_len - file_len
                
                break

    else:
        idx -= 1

checksum = 0

for i in range(len(blocks)):
    if blocks[i] != '.':
        checksum += i * blocks[i]

print(checksum)
    
