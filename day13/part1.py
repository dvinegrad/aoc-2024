import re

def min_cost_for_prize(prize, a, b, memo, presses):
    #print("Called", prize, a, b)
    if presses > 100:
        return (False, -1)
    
    if prize[0] < 0 or prize[1] < 0:
        return (False, -1)
        
    if prize[0] == 0 and prize[1] == 0:
        #print("nothing to press!")
        return (True, 0)
        
    if ((prize, a, b) in memo):
        #print("memoized result", memo[(prize, a, b)])
        return memo[(prize, a, b)]
        
    test_a = min_cost_for_prize((prize[0] - a[0], prize[1] - a[1]), a, b, memo, presses + 1)
    test_b = min_cost_for_prize((prize[0] - b[0], prize[1] - b[1]), a, b, memo, presses + 1)
    
    if test_a[0]:
        test_a = (True, test_a[1] + 3)
    
    if test_b[0]:
        test_b = (True, test_b[1] + 1)
    
    
    valid = [test for test in [test_a, test_b] if test[0] == True]
    
    if len(valid) == 0:
        res = (False, -1)
    else:    
        res = (True, min([test[1] for test in valid]))
    memo[(prize, a, b)] = res
    return res
    
    


with open('input.txt') as f:
    claw_strs = f.read().split("\n\n")
    
claw_data = []

for claw_input in claw_strs:
    lines = claw_input.splitlines()
    claw = dict()
    claw['A'] = tuple(map(int, re.match("Button A: X\\+(\\d+), Y\\+(\\d+)", lines[0]).groups()))
    claw['B'] = tuple(map(int, re.match("Button B: X\\+(\\d+), Y\\+(\\d+)", lines[1]).groups()))
    claw['Prize'] = tuple(map(int, re.match("Prize: X=(\\d+), Y=(\\d+)", lines[2]).groups()))
    claw_data.append(claw)
   
total_cost = 0    
for claw in claw_data:
    res = min_cost_for_prize(claw['Prize'], claw['A'], claw['B'], {}, 0)
    if res[0]:
        total_cost += res[1]
        
print(total_cost)
    
