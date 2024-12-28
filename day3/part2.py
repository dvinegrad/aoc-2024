import re

with open('input.txt') as f:
    lines = f.read().splitlines()
    
total = 0
ignore = False
exp = r"mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))"

for line in lines:
    matches = re.findall(exp, line)
    for match in matches:
        if match[2] == "do()":
            ignore = False
        elif match[3] == "don't()":
            ignore = True
        elif not ignore:
            total += int(match[0]) * int(match[1]) 
       
print(total)
