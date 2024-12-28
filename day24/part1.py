def get_wire_value(wire, wire_values, wire_exprs):
    if wire in wire_values:
        return wire_values[wire]

    expr = wire_exprs[wire]
    left, op, right = expr.split(" ")
    lval = get_wire_value(left, wire_values, wire_exprs)
    rval = get_wire_value(right, wire_values, wire_exprs)

    if op == "XOR":
        res = lval ^ rval
    elif op == "OR":
        res = lval | rval
    else:
        res = lval & rval

    wire_values[wire] = res
    return res


with open('input.txt') as f:
    lines = f.read().splitlines()    

wire_values = dict()
wire_exprs = dict()

for line in lines:
    if ":" in line:
        wire, val = line.split(": ")
        wire_values[wire] = int(val)
    elif "->" in line:
        expr, wire = line.split(" -> ")
        wire_exprs[wire] = expr

for wire in wire_exprs.keys():
    get_wire_value(wire, wire_values, wire_exprs)

# for wire in sorted(wire_values.keys()):
#     print(f"{wire}: {wire_values[wire]}")

result = 0
for _, val in reversed(sorted([item for item in wire_values.items() if item[0].startswith("z")])):
    result <<= 1
    result += val

print(result)