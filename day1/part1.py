with open('input.txt') as f:
    lines = f.read().splitlines()
    
nums = [[int(v) for v in line.split()] for line in lines]
    
left, right = map(sorted, map(list, zip(*nums)))

distance = sum([abs(left[i] - right[i]) for i in range(len(left))])

print(distance)