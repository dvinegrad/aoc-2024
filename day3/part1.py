import re

with open('input.txt') as f:
    lines = f.read().splitlines()
    
total = 0
exp = r"mul\((\d+),(\d+)\)"

for line in lines:
    matches = re.findall(exp, line)
    for match in matches:
       total += int(match[0]) * int(match[1])
       
print(total)
