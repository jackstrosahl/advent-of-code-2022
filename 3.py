from functools import reduce


lower_off = ord("a") - 1
upper_off = ord("A") - 27
def get_priority(char):
    priority = ord(char)
    if priority < lower_off:
        priority -= upper_off
    else:
        priority -= lower_off
    return priority

with open("3.txt") as f:
    sacks = [line.rstrip("\n") for line in f]

ans = 0
for sack in sacks:
    compartment_size = len(sack) // 2
    first_compartment = set(sack[:compartment_size])
    common = next(char for char in sack[compartment_size:] if char in first_compartment)
    ans += get_priority(common)

print(ans)

ans = 0
for i in range(0,len(sacks),3):
    group = sacks[i:i+3]
    common = next(char for char in reduce(lambda a, b: set(b).intersection(a),group))
    ans += get_priority(common)

print(ans)