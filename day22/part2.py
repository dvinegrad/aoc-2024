from collections import defaultdict, Counter
from functools import reduce

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def get_next_secret(secret):
    secret = mix(secret * 64, secret)
    secret = prune(secret)

    secret = mix(secret, secret // 32)
    secret = prune(secret)

    secret = mix(secret, secret * 2048)
    return prune(secret)

def get_n_secret_costs(secret, n):
    res = [secret % 10]
    for i in range(n):
        secret = get_next_secret(secret)
        res.append(secret % 10)

    return res

def get_deltas(secret_nums):
    delta_cost_map = defaultdict(int)
    for k, v in map(lambda i: (tuple(map(lambda j: secret_nums[j + 1] - secret_nums[j], range(i, i+4))), secret_nums[i + 4]), range(len(secret_nums) - 4)):
        if k not in delta_cost_map:
            delta_cost_map[k] = v

    return delta_cost_map

def combine_counts(counts1, counts2):
    ctr1 = Counter(counts1)
    ctr2 = Counter(counts2)
    ctr1.update(ctr2)
    return dict(ctr1)


with open('input.txt') as f:
    initial_nums = [int(line) for line in f.read().splitlines()]

all_deltas = map(lambda initial: get_deltas(get_n_secret_costs(initial, 2000)), initial_nums)
all_costs = reduce(lambda c1, c2: combine_counts(c1, c2), all_deltas)

print(max(all_costs.values()))