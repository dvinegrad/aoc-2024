import heapq

def dijkstra(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = ((i, j), (0, 1))
    
    pq = [(0, start)]
    costs = { start: 0 }

    while len(pq) > 0:
        cost, (pos, direction) = heapq.heappop(pq)

        if grid[pos[0]][pos[1]] == 'E':
            return cost

        turns = [(1000, (pos, turn)) for turn in [(direction[1] * i, direction[0] * i) for i in [-1,1]]]

        step = tuple(map(sum, zip(pos, direction)))
        
        neighbors = turns + ([(1, (step, direction))] if grid[step[0]][step[1]] != '#' else [])
        for neighbor in neighbors:
            next_cost = cost + neighbor[0]
            if next_cost < costs.get(neighbor[1], float('inf')):
                heapq.heappush(pq, (next_cost, neighbor[1]))
                costs[neighbor[1]] = next_cost

    print("Could not find min path")
    return None




with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]

print(dijkstra(grid))


