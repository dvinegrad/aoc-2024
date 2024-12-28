def is_safe(report):
    deltas = [a-b for a,b in zip(report, report[1:])]
    return all([1 <= delta <=3 for delta in deltas]) or all([-3 <= delta <= -1 for delta in deltas])

with open('input.txt') as f:
    lines = f.read().splitlines()
    
reports = [[int(v) for v in line.split()] for line in lines]
num_safe = sum(is_safe(report) for report in reports)
print(num_safe)
