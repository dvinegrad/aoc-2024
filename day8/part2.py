import math

def get_antinodes(pt_a, pt_b, n_rows, n_cols):
    diff = (pt_b[0] - pt_a[0], pt_b[1] - pt_a[1])
    gcd = math.gcd(diff[0], diff[1])
    delta = (diff[0] / gcd, diff[1] / gcd)
    
    antinodes = set()
    cur = pt_a
    while cur[0] >= 0 and cur[0] < n_rows and cur[1] >= 0 and cur[1] < n_cols:
        antinodes.add(cur)
        cur = (cur[0] - delta[0], cur[1] - delta[1])
    
    while cur[0] >= 0 and cur[0] < n_rows and cur[1] >= 0 and cur[1] < n_cols:
        antinodes.add(cur)
        cur = (cur[0] + delta[0], cur[1] + delta[1])
        
    return antinodes
    

with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]
    
n_rows = len(grid)
n_cols = len(grid[0])

antenna_locs = {}
antinodes = set()

for i in range(n_rows):
    for j in range(n_cols):    
        if not grid[i][j] == '.':
            antenna_locs.setdefault(grid[i][j], []).append((i, j))
    
for letter, letter_locs in antenna_locs.items():
     for pt_1 in letter_locs:
         for pt_2 in letter_locs:
             if not pt_1 == pt_2:
                 antinodes.update(get_antinodes(pt_1, pt_2, n_rows, n_cols))
             
print(len(antinodes))