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
mid_x = x_len // 2
mid_y = y_len // 2
num_seconds = 100
quadrant_counts = [0, 0, 0, 0]

for i in range(len(positions)):
    pos = ((positions[i][0] + num_seconds * velocities[i][0]) % x_len, (positions[i][1] + num_seconds * velocities[i][1]) % y_len)

    if pos[0] < mid_x and pos[1] < mid_y:
        quadrant_counts[0] += 1
    
    elif pos[0] < mid_x and pos[1] > mid_y:
        quadrant_counts[1] += 1

    elif pos[0] > mid_x and pos[1] < mid_y:
        quadrant_counts[2] += 1

    elif pos[0] > mid_x and pos[1] > mid_y:
        quadrant_counts[3] += 1

print(reduce(mul, quadrant_counts))




    

    
