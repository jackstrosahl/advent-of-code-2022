from collections import deque
from sortedcontainers import SortedList


with open("1.txt") as f:
    lines = [line.rstrip("\n") for line in f]
    lines.append("")

elf = 0
elves = []
for line in lines:
    if line == "":
        elves.append(elf)
        elf = 0
        continue
    elf += int(line)

print(max(elves))

top = SortedList()
for elf in elves:
    if len(top) < 3:
        top.add(elf)
        continue
    for other in reversed(top):
        if elf > other:
            top.pop(0)
            top.add(elf)
            break

print(sum(top))