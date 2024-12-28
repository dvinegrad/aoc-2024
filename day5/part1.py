def is_valid(update, rules):
    all_pages = set(update)
    seen_pages = set()
    
    for cur in update:
        if cur in rules:
            for n in rules[cur]:
                if n in all_pages and not n in seen_pages:
                    return False
        
        seen_pages.add(cur)
    
    return True

with open('input.txt') as f:
    lines = f.read().splitlines()
    
rules = {}
updates = []

for line in lines:
    if "|" in line:
        x, y = map(int, line.split("|"))
        if not y in rules:
            rules[y] = []
        rules[y] += [x]
        
    elif len(line) > 0:
        updates.append(list(map(int, line.split(","))))
        
total = 0
for update in updates:
    if is_valid(update, rules):
        total += update[len(update) // 2]
        
print(total)


