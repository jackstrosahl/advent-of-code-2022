with open("4-test.txt") as f:
    pairs = [[[int(i) for i in section_range.split("-")] for section_range in line.rstrip("\n").split(",")] for line in f]

for pair in pairs:
    sections = [set(range()) for section_range in pair]
