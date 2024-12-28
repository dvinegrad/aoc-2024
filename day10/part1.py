MAX_HEIGHT = 9

def get_reachable_max(grid, i, j):
    if grid[i][j] == MAX_HEIGHT:
        return set([(i, j)])
        
    s = set()
    adjacent = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    
    for pt in adjacent:
        if pt[0] >= 0 and pt[0] < len(grid) and pt[1] >= 0 and pt[1] < len(grid) and grid[pt[0]][pt[1]] == grid[i][j] + 1:
            s.update(get_reachable_max(grid, pt[0], pt[1]))
    
    return s

with open('input.txt') as f:
    grid = [[int(c) if c != '.' else -1 for c in line] for line in f.read().splitlines()]

total_scores = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            reachable = get_reachable_max(grid, i, j)
            total_scores += len(reachable)
            
print(total_scores)
