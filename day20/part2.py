

def bfs(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = ((i, j))
    
    visited = set([start])
    frontier = [[start]]

    while len(frontier) > 0:
        path = frontier.pop(0)
        cur = path[-1]

        if grid[cur[0]][cur[1]] == 'E':
            return path            

        neighbors = [tuple(map(sum, zip(cur, direction))) for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        neighbors = [pos for pos in neighbors if pos[0] in range(len(grid)) and pos[1] in range(len(grid[0])) and grid[pos[0]][pos[1]] != '#']
        
        for neighbor in neighbors:
            if neighbor not in visited:
                frontier.append(path + [neighbor])
                visited.add(neighbor)

    return None

def get_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]

shortest_no_cheat_path = bfs(grid)
ct_saved = 0

for i in range(len(shortest_no_cheat_path)):
    for j in range(i + 1, len(shortest_no_cheat_path)):
        dist = get_manhattan_distance(shortest_no_cheat_path[i], shortest_no_cheat_path[j])
        if dist <= 20 and j - i - dist >= 100:
            ct_saved += 1
        
print(ct_saved)