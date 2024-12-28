def get_next_array(stones):
    res = []
    
    for stone in stones:
        if stone == 0:
            res.append(1)
        
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            res.append(int(stone_str[0:len(stone_str)//2]))
            res.append(int(stone_str[len(stone_str)//2:]))
        
        else:
            res.append(stone * 2024)
            
    return res
            


with open('input.txt') as f:
    stones = [int(s) for s in f.read().split()]


for i in range(25):
    stones = get_next_array(stones)

print(len(stones))