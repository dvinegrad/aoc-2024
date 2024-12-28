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

def get_sides(region):
    sides = 0
    visited_edges = set()
    
    sorted_region = sorted(list(region))
    
    for loc in sorted_region:
        above = (loc[0] - 1, loc[1])
        if above not in region:
            visited_edges.add((above, 'bottom'))
            if ((above[0], above[1] - 1), 'bottom') not in visited_edges and ((above[0], above[1] + 1), 'bottom') not in visited_edges:
                sides += 1

        below = (loc[0] + 1, loc[1])
        if below not in region:
            visited_edges.add((below, 'top'))
            if ((below[0], below[1] - 1), 'top') not in visited_edges and ((below[0], below[1] + 1), 'top') not in visited_edges:
                sides += 1

        left = (loc[0], loc[1] - 1)
        if left not in region:
            visited_edges.add((left, 'right'))
            if ((left[0] - 1, left[1]), 'right') not in visited_edges and ((left[0] + 1, left[1]), 'right') not in visited_edges:
                sides += 1

        
        right = (loc[0], loc[1] + 1)
        if right not in region:
            visited_edges.add((right, 'left'))
            if ((right[0] - 1, right[1]), 'left') not in visited_edges and ((right[0] + 1, right[1]), 'left') not in visited_edges:
                sides += 1
                        
    return sides

def get_corners(region):
    corners = 0
    for loc in region:
        outer_top_left = [((0, -1), False), ((-1, 0), False)]
        outer_top_right = [((0, 1), False), ((-1, 0), False)]
        outer_bottom_right = [((0, 1), False), ((1, 0), False)]
        outer_bottom_left = [((0, -1), False), ((1, 0), False)]

        inner_top_left = [((0, 1), True), ((1, 0), True), ((1, 1), False)]
        inner_top_right = [((0, -1), True), ((1, 0), True), ((1, -1), False)]
        inner_bottom_right = [((0, -1), True), ((-1, 0), True), ((-1, -1), False)]
        inner_bottom_left = [((0, 1), True), ((-1, 0), True), ((-1, 1), False)]

        all_neighbors = [outer_top_left, outer_top_right, outer_bottom_right, outer_bottom_left, inner_top_left, inner_top_right, inner_bottom_right, inner_bottom_left]

        corners += sum([all([((loc[0] + pt[0][0], loc[1] + pt[0][1]) in region) == pt[1] for pt in neighbor]) for neighbor in all_neighbors])

    return corners
        
        
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
    price = get_area(region) * get_corners(region)
    total_price += price
    
print(total_price)
    
