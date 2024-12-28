def calculate_one_itr(a):
    b = a % 8
    b = b ^ 2
    c = a // (2 ** b)
    b = b ^ 7
    b = b ^ c
    a = a // (2 ** 3)
    return (b % 8)
    
with open('input.txt') as f:
    lines = f.read().splitlines()

instructions = list(map(int, lines[4].split(": ")[1].split(",")))

a_vals = [0]

for i in reversed(range(len(instructions))):
    next_a_vals = [] 
    for a_val in a_vals:
        for a in range(a_val, a_val + 8):
            if calculate_one_itr(a) == instructions[i]:
                next_a_vals += [a * 8]
    a_vals = next_a_vals

print(min(a_vals) // 8)