with open("4.txt") as f:
    pairs = [[[int(i) for i in section_range.split("-")] for section_range in line.rstrip("\n").split(",")] for line in f]

ans_p1 = 0
ans_p2 = 0
for pair in pairs:
    sections = [set(range(start, end+1)) for start,end in pair]
    common = sections[0].intersection(sections[1])
    if common in sections:
        ans_p1 += 1
    if common:
        ans_p2 += 1

print(ans_p1)
print(ans_p2)
