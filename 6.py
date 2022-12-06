from re import search

def marker_regex(n):
    regex = ""
    for i in range(n):
        regex += r"(.)"
        if i > 0:
            regex += r"(?!"
            regex += r"|".join(fr"\{j}" for j in range(1,i+1))
            regex += r")"

    return regex

with open("6-test.txt") as f:
    lines = [line.rstrip("\n") for line in f]

for line in lines:
    print(search(r"(.)(?!\1)(.)(?!\1|\2)(.)(?!\1|\2|\3)(.)", line).end())