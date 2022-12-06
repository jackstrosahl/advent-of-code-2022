from collections import deque
from re import split


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

moves = [tuple(int(num) for num in split(r"[^0-9]+",move_line)[1:]) for move_line in move_lines]

for count, source, dest in moves:
    for _ in range(count):
        stacks[dest - 1].append(stacks[source - 1].pop())

print("".join(stack[-1] for stack in stacks))