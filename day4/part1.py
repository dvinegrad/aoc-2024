import itertools

def is_word_match(grid, word, pos, direction):
    cur = ''
    idx = 0
    
    while word.startswith(cur) and not cur == word:
        next_pos = (pos[0] + direction[0] * idx, pos[1] + direction[1] * idx)
        if not (0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0])):
            break
        
        cur += grid[next_pos[0]][next_pos[1]]
        idx += 1
        
    return cur == word         
    

with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]
    

directions = [t for t in itertools.product(range(-1,2), range(-1,2)) if not (t[0] == 0 and t[1] == 0)]

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        for direction in directions:
            if is_word_match(grid, 'XMAS', (i, j), direction):
                total += 1

print(total)


