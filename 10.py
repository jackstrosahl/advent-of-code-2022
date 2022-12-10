with open("10.txt") as f:
    instructions = [line.rstrip("\n").split(" ") for line in f]

x = 1
clock = 1
ans = 0

for instruction in instructions:
    op = instruction[0]
    if op == "noop":
        length = 1
        value = 0
    else:
        length = 2
        value = int(instruction[1])
    for _ in range(length):
        if clock <= 220 and (clock-20) % 40 == 0:
            ans += clock * x
        clock += 1
    x += value

print(ans)