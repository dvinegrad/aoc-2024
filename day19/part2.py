def num_possible_patterns(pattern, towels, memo):
    if pattern == "":
        return 1

    if pattern in memo:
        return memo[pattern]

    res = sum([num_possible_patterns(pattern[len(t):], towels, memo) if pattern.startswith(t) else 0 for t in towels])
    memo[pattern] = res
    return res


with open('input.txt') as f:
    lines = f.read().splitlines()
    
towels = [s.strip() for s in lines[0].split(",")]

patterns = lines[2:]

print(sum([num_possible_patterns(p, towels, dict()) for p in patterns]))