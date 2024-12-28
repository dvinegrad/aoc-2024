class Gate:
    def __init__(self, inputs, op, label):
        self.inputs = inputs
        self.op = op
        self.label = label

    def __eq__(self, other):
        if type(self) == type(other):
            return self.op == other.op and self.inputs == other.inputs and self.label == self.label
        else:
            return False
    
    def __hash__(self):
        return hash((self.op, self.inputs, self.label))

    def __str__(self):
        first, second = sorted(map(str, self.inputs))
        return f"({first} {self.op} {second})"

    

class Circuit:
    def __init__(self, input_lines):
        self.input_digit_xors = []
        self.input_digit_ands = []
        self.output_to_expr = {}
        self.expr_to_output = {}
        self.invalid_input_ands = {}
        self.result_gates = []
        self.carry_gates = []
        self.__parse_input(input_lines)

    def __parse_input(self, input_lines):
        for line in input_lines:
            if "->" in line:
                expr, wire = line.split(" -> ")
                left, op, right = expr.split(" ")

                left, right = sorted((left, right))
                self.output_to_expr[wire] = (left, right, op)
                self.expr_to_output[(left, right, op)] = wire   

                input_exprs = dict({(k, v) for (k, v) in self.expr_to_output.items() if k[0].startswith("x")})  
                
        for input_expr in sorted(input_exprs.items()):
            idx = int(input_expr[0][0][1:])
            op = input_expr[0][2]
            res = input_expr[1]
            if op == 'AND':
                self.input_digit_ands.append(res)
                if (res.startswith("z")):
                    self.invalid_input_ands[idx] = res
            elif op == 'XOR':
                self.input_digit_xors.append(res)

        for i in range(len(self.input_digit_xors) + 1):
            input_bits_xor_gate = Gate((f"x{i:02}", f"y{i:02}"), "XOR", None)
            input_bits_and_gate = Gate((f"x{i:02}", f"y{i:02}"), "AND", None)
            if i == 0:
                result_gate = input_bits_xor_gate
                carry_gate = input_bits_and_gate
            else:
                result_gate = Gate((input_bits_xor_gate, self.carry_gates[i - 1]), "XOR", None)
                carry_gate = Gate((input_bits_and_gate, Gate((input_bits_xor_gate, self.carry_gates[i - 1]), "AND", None)), "OR", None)

            self.result_gates.append(result_gate)
            self.carry_gates.append(carry_gate)
        
        print(self.result_gates[-1])


with open('input.txt') as f:
    lines = f.read().splitlines()  

circuit = Circuit(lines)  

output_to_expr = dict()
expr_to_output = dict()

for line in lines:
    if "->" in line:
        expr, wire = line.split(" -> ")
        left, op, right = expr.split(" ")

        left, right = sorted((left, right))
        output_to_expr[wire] = (left, right, op)
        expr_to_output[(left, right, op)] = wire

input_exprs = dict({(k, v) for (k, v) in expr_to_output.items() if k[0].startswith("x")})

input_digit_xors = []
input_digit_ands = []
output_digit_carries = []
output_digit_results = []

invalid_input_ands = {}

for input_expr in sorted(input_exprs.items()):
    idx = int(input_expr[0][0][1:])
    op = input_expr[0][2]
    res = input_expr[1]
    if op == 'AND':
        input_digit_ands.append(res)
        if (res.startswith("z")):
            print(f"{res} is an AND!")
            invalid_input_ands[idx] = res
    elif op == 'XOR':
        input_digit_xors.append(res)

print(input_digit_xors)
print(input_digit_ands)

swaps = {}

for i in range(len(input_digit_xors)):
    if i == 0:
        output_digit_results.append(input_digit_xors[0])
        output_digit_carries.append(input_digit_ands[0])
    else:
        result_op = (*sorted((input_digit_xors[i], output_digit_carries[i - 1])), "XOR")
        if result_op not in expr_to_output:
            incorrect = output_to_expr[f"z{i:02}"]
            swap1 = set(result_op).difference(set(incorrect)).pop()
            swap2 = set(incorrect).difference(set(result_op)).pop()
            print(f"need to swap {swap1} and {swap2}")
            swaps[swap1] = swap2
            swaps[swap2] = swap1
            result_output = expr_to_output[incorrect]
            if input_digit_xors[i] == swap1:
                print("swapping input digit xors to", swap2)
                input_digit_xors[i] = swap2
            if input_digit_ands[i] == swap2:
                print("swapping input digit ands to", swap1)
                input_digit_ands[i] = swap1

        else:
            result_output = expr_to_output[result_op]

        if not result_output.startswith("z"):
            expected_output = f"z{i:02}"
            if i in invalid_input_ands and expected_output == invalid_input_ands[i]:
                print(f"need to swap {expected_output} and {result_output}")
                swaps[result_output] = expected_output
                swaps[expected_output] = result_output
                print("swapping input digit ands to", result_output)
                input_digit_ands[i] = result_output
                print("swapping result")
                result_output = expected_output

            else:
                print(f"need to swap {expected_output} and {result_output}")
                swaps[result_output] = expected_output
                swaps[expected_output] = result_output
                print("swapping result")
                result_output = expected_output

        elif int(result_output[1:]) != i:
            if result_output in swaps:
                expr_to_output[result_op] = swaps[result_output]
            else:
                expected_output = f"z{i:02}"
                print(f"need to swap {result_output} and {expected_output}")
                swaps[expected_output] = result_output
                swaps[result_output] = expected_output
                expr_to_output[result_op] = expected_output

        output_digit_results.append(result_output)

        rhs_op = (*sorted((input_digit_xors[i], output_digit_carries[i - 1])), "AND")
        rhs_output = expr_to_output[rhs_op]
        if rhs_output in swaps:
            print("swapping rhs")
            rhs_output = swaps[rhs_output]

        carry_op = (*sorted((input_digit_ands[i], rhs_output)), "OR")
        carry_output = expr_to_output[carry_op]
        if carry_output in swaps:
            print("swapping carry")
            carry_output = swaps[carry_output]

        output_digit_carries.append(carry_output)

        print(f"{i:02} is in {result_output} with carry {carry_output}")

print(",".join(sorted(swaps.keys())))

