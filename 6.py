from re import search

def marker_regex(n):
    regex = ""
    for i in range(n):
        if i > 0:
            regex += r"(?!"
            regex += r"|".join(fr"\{j}" for j in range(1,i+1))
            regex += r")"
        regex += r"(.)"
    return regex

with open("6.txt") as f:
    lines = [line.rstrip("\n") for line in f]

for line in lines:
    print(search(marker_regex(4), line).end())

print()

for line in lines:
    print(search(marker_regex(14), line).end())