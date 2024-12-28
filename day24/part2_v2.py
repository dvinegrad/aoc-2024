def get_expr_for_output(output):
    return output_to_expr[swaps.get(output, output)]

def get_output_for_expr(expr):
    output = expr_to_output[expr]
    return swaps.get(output, output)

def swap(out_a, out_b):
    print(f"SWAP: {out_a} for {out_b}")
    swaps[out_a] = out_b
    swaps[out_b] = out_a

def find_matching_expr(output, op):
    matching = [expr for expr in expr_to_output if expr[2] == op and output in (expr[0], expr[1])]
    if len(matching) == 0:
        return None
    assert len(matching) == 1
    return matching[0]

with open('input.txt') as f:
    lines = f.read().splitlines()    

output_to_expr = dict()
expr_to_output = dict()
swaps = dict()
carries = []

max_input_bit_index = -1

for line in lines:
    if "->" in line:
        expr, wire = line.split(" -> ")
        left, op, right = expr.split(" ")

        left, right = sorted((left, right))
        output_to_expr[wire] = (left, right, op)
        expr_to_output[(left, right, op)] = wire
    if ":" in line:
        max_input_bit_index = max(max_input_bit_index, int(line.split(":")[0][1:]))

num_input_bits = max_input_bit_index + 1

for i in range(num_input_bits):
    z_output = f"z{i:02}"
    input_xor_expr = (f"x{i:02}", f"y{i:02}", "XOR")
    input_and_expr = (f"x{i:02}", f"y{i:02}", "AND")

    input_xor_output = get_output_for_expr(input_xor_expr)
    input_and_output = get_output_for_expr(input_and_expr)

    if i == 0:
        if z_output == input_xor_output:
            carries.append(input_and_output)
            continue
        else:
            raise ValueError("Error in first digits")

    result_expr = find_matching_expr(input_xor_output, "XOR")
    if result_expr == None:
        result_expr = find_matching_expr(carries[i - 1], "XOR")
        actual_input_xor_output = result_expr[1] if result_expr[0] == carries[i - 1] else result_expr[0]
        swap(actual_input_xor_output, input_xor_output)
    else:
        carry_input = result_expr[1] if result_expr[0] == input_xor_output else result_expr[0]
        if carry_input != carries[i - 1]:
            swap(carry_input, carries[i - 1])
            carries[i - 1] = carry_input

    if z_output != get_output_for_expr(result_expr):
        swap(z_output, get_output_for_expr(result_expr))
    
    intermediate_carry_expr = (*sorted((get_output_for_expr(input_xor_expr), carries[i - 1])), "AND")
    intermediate_carry_output = get_output_for_expr(intermediate_carry_expr)

    carry_expr = find_matching_expr(intermediate_carry_output, "OR")
    if carry_expr == None:
        print("TODO")
    else:
        expected_input_and_output = carry_expr[1] if carry_expr[0] == intermediate_carry_output else carry_expr[0]
        if expected_input_and_output != get_output_for_expr(input_and_expr):
            swap(get_output_for_expr(input_and_expr), expected_input_and_output)

    carry_expr = (*sorted((get_output_for_expr(input_and_expr), intermediate_carry_output)), "OR")    
    carry_output = get_output_for_expr(carry_expr)

    carries.append(carry_output)
    
print(*sorted(swaps.keys()), sep=",")
