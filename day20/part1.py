

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

def get_shortest_for_cheat(grid, cheat, no_cheat_path):
    wall = cheat[0]
    wall_neighbors = list(filter(lambda loc: loc in no_cheat_path, [tuple(map(sum, zip(wall, direction))) for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]]))
    before_cheat_idx = min([no_cheat_path.index(loc) for loc in wall_neighbors])

    after_cheat = cheat[1]

    after_cheat_idx = no_cheat_path.index(after_cheat)

    return no_cheat_path[0:before_cheat_idx + 1] + [wall] + no_cheat_path[after_cheat_idx:]


with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]

memo = {}

shortest_no_cheat_path = bfs(grid)
target = len(shortest_no_cheat_path) - 1
ct_saved = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '#':
            neighbors = [tuple(map(sum, zip((i, j), direction))) for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
            neighbors = list(filter(lambda pos: pos[0] in range(len(grid)) and pos[1] in range(len(grid[0])) and grid[pos[0]][pos[1]] != '#', neighbors))
            for neighbor in neighbors:
                path = get_shortest_for_cheat(grid, ((i, j), neighbor), shortest_no_cheat_path)
                if len(path) - 1 <= target - 100:
                    ct_saved += 1

print(ct_saved)