import math

def is_valid(target, sum_so_far, vals):
    if len(vals) == 0:
        return target == sum_so_far
        
    if sum_so_far > target:
        return False
        
        
    return is_valid(target, sum_so_far + vals[0], vals[1:]) or is_valid(target, sum_so_far * vals[0], vals[1:]) or is_valid(target, int(f'{sum_so_far}' + f'{vals[0]}'), vals[1:])
    

with open('input.txt') as f:
    lines = f.read().splitlines()
    
    
total = 0

for line in lines:
    test_val = int(line.split(": ")[0])
    vals = list(map(int, line.split(": ")[1].split()))
    if is_valid(test_val, 0, vals):
        total += test_val
        
print(total)