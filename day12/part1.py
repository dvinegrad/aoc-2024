def add_to_region_from(grid, loc, region, visited):
    region.add(loc)
    visited.add(loc)
    
    neighbors = [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]
    neighbors = [pt for pt in neighbors if pt[0] in range(len(grid)) and pt[1] in range(len(grid))]
    
    for neighbor in neighbors:
        if grid[loc[0]][loc[1]] == grid[neighbor[0]][neighbor[1]] and not neighbor in visited:
            add_to_region_from(grid, neighbor, region, visited)
            
def get_area(region):
    return len(region)
    
def get_perimeter(region):
    perimeter = 0
    
    for loc in region:
        neighbors = [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]
        perimeter += len([pt for pt in neighbors if pt not in region])
    return perimeter


with open('input.txt') as f:
    grid = [[c for c in line] for line in f.read().splitlines()]


visited = set()
regions = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not (i, j) in visited:
            region = set()
            add_to_region_from(grid, (i, j), region, visited)
            regions.append(region)
            
        visited.add((i, j))
        
total_price = 0

for region in regions:
    total_price += get_area(region) * get_perimeter(region)
    
print(total_price)
    
