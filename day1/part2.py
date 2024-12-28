with open('input.txt') as f:
    lines = f.read().splitlines()
    
nums = [[int(v) for v in line.split()] for line in lines]
    
left, right = map(list, zip(*nums))

right_counts = dict()
for r in right:
    right_counts[r] = right_counts.get(r, 0) + 1
    

similarity = 0
for l in left:
    similarity += l * right_counts.get(l, 0)
    
print(similarity)

