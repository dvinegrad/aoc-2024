def is_pattern_possible(pattern, towels, visited):
    if pattern == "":
        return True

    visited.add(pattern)

    return any([pattern.startswith(t) and pattern[len(t):] not in visited and is_pattern_possible(pattern[len(t):], towels, visited) for t in towels])


with open('input.txt') as f:
    lines = f.read().splitlines()
    
towels = [s.strip() for s in lines[0].split(",")]

patterns = lines[2:]

print(sum([is_pattern_possible(p, towels, set()) for p in patterns]))