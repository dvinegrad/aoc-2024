def bfs(byte_locs, x_len, y_len):
    start = (0, 0)
    end = (x_len - 1, y_len - 1)
    visited = set()
    frontier = [[start]]

    while len(frontier) > 0:
        path = frontier.pop(0)
        cur = path[-1]
        
        if cur == end:
            return path
        
        visited.add(cur)
        

        neighbors = [tuple(map(sum, zip(cur, direction))) for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        neighbors = [pos for pos in neighbors if pos[0] in range(x_len) and pos[1] in range(y_len) and pos not in byte_locs]

        for neighbor in neighbors:
            if neighbor not in visited:
                frontier.append(path + [neighbor])
                visited.add(neighbor)

    print("no path found")
    return None




with open('input.txt') as f:
    lines = f.read().splitlines()
    
byte_locs = [tuple(map(int, line.split(","))) for line in lines]

x_len = 71
y_len = 71

print(len(bfs(set(byte_locs[0:1024]), x_len, y_len)) - 1)
