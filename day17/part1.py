ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7

def get_combo_operand(operand, reg):
    if 0 <= operand <= 3:
        return operand

    if 4 <= operand <= 6:
        return reg[chr(ord('A') + operand - 4)]    
    
    raise ValueError(f"Unexpected operand {operand}")

with open('input.txt') as f:
    lines = f.read().splitlines()

reg = { 'A': int(lines[0].split(": ")[1]), 'B': int(lines[1].split(": ")[1]), 'C': int(lines[2].split(": ")[1])}
instructions = list(map(int, lines[4].split(": ")[1].split(",")))

output = []
instr_ptr = 0

while instr_ptr < len(instructions):
    jump = False
    opcode, operand = instructions[instr_ptr:instr_ptr + 2]

    if opcode == ADV:
        reg['A'] = reg['A'] // (2 ** get_combo_operand(operand, reg))

    elif opcode == BXL:
        reg['B'] = reg['B'] ^ operand

    elif opcode == BST:
        reg['B'] = get_combo_operand(operand, reg) % 8

    elif opcode == JNZ:
        if reg['A'] != 0:
            instr_ptr = operand
            jump = True

    elif opcode == BXC:
        reg['B'] = reg['B'] ^ reg['C']

    elif opcode == OUT:
        output += [get_combo_operand(operand, reg) % 8]

    elif opcode == BDV:
        reg['B'] = reg['A'] // (2 ** get_combo_operand(operand, reg))

    elif opcode == CDV:
        reg['C'] = reg['A'] // (2 ** get_combo_operand(operand, reg))

    else:
        raise ValueError(f"Unexpected opcode {opcode}")

    if not jump:
        instr_ptr += 2

print(",".join(map(str, output)))