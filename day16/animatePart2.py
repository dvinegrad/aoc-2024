import heapq
import itertools
import time

def dijkstra(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = ((i, j), (0, 1))
    
    pq = [(0, (start, [start]))]
    costs = { start: 0 }

    all_shortest_paths = []
    shortest_cap = float('inf')

    while len(pq) > 0:
        cost, ((pos, direction), cur_path) = heapq.heappop(pq)

        if cost > shortest_cap:
            break

        if grid[pos[0]][pos[1]] == 'E':
            all_shortest_paths += [cur_path]
            shortest_cap = cost

        turns = [(1000, (pos, turn)) for turn in [(direction[1] * i, direction[0] * i) for i in [-1,1]]]
        step = tuple(map(sum, zip(pos, direction)))
        
        neighbors = turns + ([(1, (step, direction))] if grid[step[0]][step[1]] != '#' else [])
        for neighbor in neighbors:
            next_cost = cost + neighbor[0]
            if next_cost <= costs.get(neighbor[1], float('inf')):
                heapq.heappush(pq, (next_cost, (neighbor[1], cur_path + [neighbor[1]])))
                costs[neighbor[1]] = next_cost

    return all_shortest_paths

def print_grid(grid, positions):
    for i in range(len(grid)):
        #print('\033[31mHello World but Red!\033[0m')
        for j in range(len(grid[i])):
            is_occupied = False
            for pos in positions:
                if pos[0] == (i, j):
                    print(f"\033[38;5;28mO\033[0m", end="")
                    is_occupied = True
                    break

            if not is_occupied:
                print(grid[i][j], end="")
        print("\n", end="")


with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]

shortest_paths = dijkstra(grid)
visited = set()

for path in shortest_paths:
    for v in path:
        visited.add(v[0])

ct = 0

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if (i, j) in visited:
#             print("O", end="")
#             ct += 1
#         else:
#             print(grid[i][j], end="")
#     print("\n", end="")

# print(ct)

printed_once = False
for position in shortest_paths[0]:
    if printed_once:
        print(f"\033[99A", end="")
    print_grid(grid, [position])
    time.sleep(1)
    printed_once = True


