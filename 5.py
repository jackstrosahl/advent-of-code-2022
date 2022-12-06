from collections import deque
from copy import deepcopy
from re import split

def stacks_string(stacks):
    return "".join(stack[-1] if stack else " " for stack in stacks)

with open("5.txt") as f:
    lines = [line.rstrip("\n") for line in f]

for i, line in enumerate(lines):
    if line == "":
        sep_i = i
        break

crate_lines = lines[:sep_i-1]
move_lines = lines[sep_i+1:]
num_crates = len(lines[sep_i-1].replace(" ",""))

stacks = [deque() for _ in range(num_crates)]

for crate_line in crate_lines:
    for i, crate in enumerate(crate_line[1::4]):
        if crate == " ":
            continue
        stacks[i].appendleft(crate)

stacks_p1 = deepcopy(stacks)
moves = [tuple(int(num) for num in split(r"[^0-9]+",move_line)[1:]) for move_line in move_lines]

for count, source, dest in moves:
    for _ in range(count):
        stacks_p1[dest - 1].append(stacks_p1[source - 1].pop())


print(stacks_string(stacks_p1))

stacks_p2 = deepcopy(stacks)
for count, source, dest in moves:
    moving = deque()
    for _ in range(count):
        moving.appendleft(stacks_p2[source - 1].pop())
    stacks_p2[dest - 1].extend(moving)

print(stacks_string(stacks_p2))