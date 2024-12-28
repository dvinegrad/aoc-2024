import re

def min_cost_for_prize(prize, a, b):
    prize_x = prize[0]
    prize_y = prize[1]
    
    a_x = a[0]
    a_y = a[1]
    b_x = b[0]
    b_y = b[1]    
    
    if (prize_x * b_y - b_x * prize_y) % (a_x * b_y - b_x * a_y) != 0:
        return (False, -1)
            
    a_val = (prize_x * b_y - b_x * prize_y) // (a_x * b_y - b_x * a_y)
    
    if (prize_x - a_x * a_val) % b_x != 0:
        return (False, -1)
    
    b_val = (prize_x - a_x * a_val) // b_x
        
    return (True, 3 * a_val + b_val)


with open('input.txt') as f:
    claw_strs = f.read().split("\n\n")
    
claw_data = []

for claw_input in claw_strs:
    lines = claw_input.splitlines()
    claw = dict()
    claw['A'] = tuple(map(int, re.match("Button A: X\\+(\\d+), Y\\+(\\d+)", lines[0]).groups()))
    claw['B'] = tuple(map(int, re.match("Button B: X\\+(\\d+), Y\\+(\\d+)", lines[1]).groups()))
    claw['Prize'] = tuple(map(lambda n: n + 10000000000000, map(int, re.match("Prize: X=(\\d+), Y=(\\d+)", lines[2]).groups())))
    claw_data.append(claw)
   
total_cost = 0    
for claw in claw_data:
    res = min_cost_for_prize(claw['Prize'], claw['A'], claw['B'])
    if res[0]:
        total_cost += res[1]
        
print(total_cost)
    
