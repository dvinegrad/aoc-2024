def get_next_arr_for_stone(stone):
    if stone == 0:
        return [1]
    
    stone_str = str(stone)
    l = len(stone_str)
    if l % 2 == 0:
        return [int(stone_str[0:l//2]), int(stone_str[l//2:])]
    
    return [stone * 2024]

with open('input.txt') as f:
    stones = [int(v) for v in f.read().split()]

stones_dict = {}
for stone in stones:
    stones_dict.setdefault(stone, 0)
    stones_dict[stone] += 1

for i in range(75):
    next_stones_dict = {}
    for stone, ct in stones_dict.items():
        next_stones = get_next_arr_for_stone(stone)
        for next in next_stones:
            next_stones_dict.setdefault(next, 0)
            next_stones_dict[next] += ct

    stones_dict = next_stones_dict

print(sum(next_stones_dict.values()))
