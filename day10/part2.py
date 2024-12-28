MAX_HEIGHT = 9

def num_ascending_to_max(grid, i, j):
    if grid[i][j] == MAX_HEIGHT:
        return 1
        
    score = 0
    adjacent = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    
    for pt in adjacent:
        if pt[0] >= 0 and pt[0] < len(grid) and pt[1] >= 0 and pt[1] < len(grid) and grid[pt[0]][pt[1]] == grid[i][j] + 1:
            score += num_ascending_to_max(grid, pt[0], pt[1])
    
    return score

with open('input.txt') as f:
    grid = [[int(c) if c != '.' else -1 for c in line] for line in f.read().splitlines()]

total_score = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            score = num_ascending_to_max(grid, i, j)
            total_score += score
            
print(total_score)
