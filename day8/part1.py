def get_antinodes(pt_a, pt_b):
    diff = (pt_b[0] - pt_a[0], pt_b[1] - pt_a[1])
    
    return [(pt_a[0] - diff[0], pt_a[1] - diff[1]), (pt_b[0] + diff[0], pt_b[1] + diff[1])]
    

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
                 antinodes.update([p for p in get_antinodes(pt_1, pt_2) if p[0] in range(n_rows) and p[1] in range(n_cols)])

print(len(antinodes))