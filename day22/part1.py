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

def get_nth_secret(secret, n):
    for i in range(n):
        secret = get_next_secret(secret)

    return secret


with open('input.txt') as f:
    initial_nums = [int(line) for line in f.read().splitlines()]
    
result = sum([get_nth_secret(s, 2000) for s in initial_nums])

print(result)