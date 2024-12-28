import sys
import time

def get_next(pos, move):
    move_dict = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    return tuple(map(sum, zip(pos, move_dict[move])))

def get_chars(c):
    if c == '@':
        return '@.'
    elif c == 'O':
        return '[]'
    else:
        return c + c

def can_push(grid, pos, move):
    if move in ['<', '>']:
        next_pos = get_next(get_next(pos, move), move)
        if grid[next_pos[0]][next_pos[1]] == '.':
            return True
        
        if grid[next_pos[0]][next_pos[1]] in ['[', ']']:
            return can_push(grid, next_pos, move)

        return False

    if move in ['^', 'v']:
        if grid[pos[0]][pos[1]] == '[':
            left, right = (pos, (pos[0], pos[1] + 1))
        else:
            left, right = ((pos[0], pos[1] - 1), pos)

        next_left = get_next(left, move)
        next_right = get_next(right, move)

        if grid[next_left[0]][next_left[1]] == '#' or grid[next_right[0]][next_right[1]] == '#':
            return False

        return (grid[next_left[0]][next_left[1]] == '.' or can_push(grid, next_left, move)) and (grid[next_right[0]][next_right[1]] == '.' or can_push(grid, next_right, move))
        
def push(grid, pos, move):
    if move in ['<', '>']:
        j = pos[1]
        while grid[pos[0]][j] != '.':
            _, j = get_next((pos[0], j), move)
        if j < pos[1]:
            grid[pos[0]][j:pos[1]] = grid[pos[0]][j+1:pos[1]+1]
        else:
            grid[pos[0]][pos[1]+1:j+1] = grid[pos[0]][pos[1]:j]

    if move in ['^', 'v']:
        if grid[pos[0]][pos[1]] == '[':
            left, right = (pos, (pos[0], pos[1] + 1))
        else:
            left, right = ((pos[0], pos[1] - 1), pos)
        
        next_left = get_next(left, move)
        next_right = get_next(right, move)

        if grid[next_left[0]][next_left[1]] == '[':
            push(grid, next_left, move)

        else:
            if grid[next_left[0]][next_left[1]] == ']':
                push(grid, next_left, move)
            
            if grid[next_right[0]][next_right[1]] == '[':
                push(grid, next_right, move)

        
        grid[next_left[0]][next_left[1]] = '['
        grid[next_right[0]][next_right[1]] = ']'
        grid[left[0]][left[1]] = '.'
        grid[right[0]][right[1]] = '.'


def print_grid(grid):
    for line in grid:
        #print('\033[31mHello World but Red!\033[0m')
        for c in line:
            if c in ['[', ']']:
                print(f"\033[38;5;220m{c}\033[0m", end="")
            elif c == '@':
                print(f"\033[38;5;28m{c}\033[0m", end="")
            elif c == '#':
                print(f"\033[38;5;167m{c}\033[0m", end="")
            elif c == '.':
                print(c, end="")
            else:
                print(c, end="")
        print("\n", end="")



grid = []
moves = []

with open('input.txt') as f:
    for line in f.read().splitlines():
        if line.startswith("#"):
            row = ""
            for c in line:
                row += get_chars(c)
            grid += [[c for c in row]]

        elif not line == "":
            moves += [c for c in line]

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '@':
            robot_pos = (i, j)
            break

printed_once = False

for move in moves:
    if printed_once:
        print(f"\033[{len(grid)}A", end="")
    next_i, next_j = get_next(robot_pos, move)
    if grid[next_i][next_j] == '.':
        grid[robot_pos[0]][robot_pos[1]] = '.'
        grid[next_i][next_j] = '@'
        robot_pos = (next_i, next_j)
    elif grid[next_i][next_j] in ['[', ']']:
        if can_push(grid, (next_i, next_j), move):
            push(grid, (next_i, next_j), move)
            grid[robot_pos[0]][robot_pos[1]] = '.'
            grid[next_i][next_j] = '@'
            robot_pos = (next_i, next_j)

    print_grid(grid)
    time.sleep(0.01)
    printed_once = True
    
        

total = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '[':
            total += 100 * i + j

print(total)




    

    
