with open("1.txt") as f:
    lines = f.readlines()

elf = 0
best = 0
for line in lines:
    if line == "\n":
        elf = 0
        continue
    elf += int(line)
    if elf > best:
        best = elf
        

print(best)