import re
from functools import reduce
from operator import mul

with open('input.txt') as f:
    lines = f.read().splitlines()

positions = []
velocities = []
for line in lines:
    m = re.match("p=(\\d+),(\\d+) v=(\\-?\\d+),(\\-?\\d+)", line)
    positions.append(tuple(map(int, m.groups()[0:2])))
    velocities.append(tuple(map(int, m.groups()[2:])))

x_len = 101
y_len = 103

initial_positions = positions[:]

for num_seconds in range(10000):
    for i in range(len(positions)):
        new_x = (initial_positions[i][0] + num_seconds * velocities[i][0]) % x_len
        new_y = (initial_positions[i][1] + num_seconds * velocities[i][1]) % y_len
        positions[i] = (new_x, new_y)

    grid = [[0] * x_len for j in range(y_len)]

    for pos in positions:
        grid[pos[1]][pos[0]] += 1

    no_dupes = True
    for y in range(y_len):
        for x in range(x_len):
            if grid[y][x] > 1:
                no_dupes = False
                break

    if no_dupes:
        print("after", num_seconds, "seconds:")
        for y in range(y_len):
            row = ""
            for x in range(x_len):
                v = grid[y][x]
                row += f'{v}' if v > 0 else '.'
            print(row)
        break




    

    
