def is_x_at(grid, i, j):
    return grid[i][j] == 'A' and ((grid[i -1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i -1][j-1] == 'S' and grid[i+1][j+1] == 'M')) and ((grid[i -1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i -1][j+1] == 'S' and grid[i+1][j-1] == 'M'))

with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]

count = 0

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if is_x_at(grid, i, j):
            count += 1

print(count)