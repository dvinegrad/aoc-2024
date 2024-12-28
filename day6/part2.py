def get_next_pos(pos, direction):
    if direction == 'v':
        return (pos[0] + 1, pos[1])
    elif direction == '^':
        return (pos[0] - 1, pos[1])
    elif direction == '<':
        return (pos[0], pos[1] - 1)
    else:
        return (pos[0], pos[1] + 1)
        
def get_next_direction(direction):
    if direction == 'v':
        return '<'
    elif direction == '<':
        return '^'
    elif direction == '^':
        return '>'
    else:
        return 'v'
        
def is_loop(grid, pos, direction):
    n_rows = len(grid)
    n_cols = len(grid[0])
    visited_with_dir = set()
    
    while 0 <= pos[0] < n_rows and 0 <= pos[1] < n_cols:
        if (pos, direction) in visited_with_dir:
            return True
        
        visited_with_dir.add((pos, direction))
        next_pos = get_next_pos(pos, direction)
    
        if 0 <= next_pos[0] < n_rows and 0 <= next_pos[1] < n_cols:
            if grid[next_pos[0]][next_pos[1]] == '#':
                direction = get_next_direction(direction)
                next_pos = pos
    
        pos = next_pos
        
    
    return False


with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]
    

n_rows = len(grid)
n_cols = len(grid[0])
    
for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] in set(['v', '^', '<', '>']):
            pos = (i, j)
            direction = grid[i][j]
            break

loop_ct = 0            

for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] == '.':
            grid[i][j] = '#'
            if is_loop(grid, pos, direction):
                loop_ct += 1
            grid[i][j] = '.'

print(loop_ct)

            
            
            