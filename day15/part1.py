def get_next(pos, move):
    move_dict = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    return tuple(map(sum, zip(pos, move_dict[move])))


grid = []
moves = []

with open('input.txt') as f:
    for line in f.read().splitlines():
        if line.startswith("#"):
            grid += [[c for c in line]]

        elif not line == "":
            moves += [c for c in line]

for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == '@':
            robot_pos = (i, j)
            break

for move in moves:
    next_i, next_j = get_next(robot_pos, move)
    if grid[next_i][next_j] == '.':
        grid[robot_pos[0]][robot_pos[1]] = '.'
        grid[next_i][next_j] = '@'
        robot_pos = (next_i, next_j)
    elif grid[next_i][next_j] == 'O':
        available = get_next((next_i, next_j), move)
        while grid[available[0]][available[1]] == 'O':
            available = get_next(available, move)
        if grid[available[0]][available[1]] == '.':
            grid[robot_pos[0]][robot_pos[1]] = '.'
            grid[next_i][next_j] = '@'
            grid[available[0]][available[1]] = 'O'
            robot_pos = (next_i, next_j)

total = 0
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 'O':
            total += 100 * i + j

print(total)




    

    
