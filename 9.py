from operator import sub

def sign(x):
    return 1 if x > 0 else -1

def add_tuples(a,b):
    return tuple(sum(x) for x in zip(a,b))

with open("9.txt") as f:
    moves = [(direction, int(distance)) for direction, distance in (line.rstrip("\n").split(" ") for line in f)]

movements = {
    "R": (1,0),
    "L": (-1,0),
    "U": (0,1),
    "D": (0,-1)
}

head = (0,0)
tail = (0,0)

visited = set()

for direction, distance in moves:
    movement = movements[direction]
    for i in range(distance):
        head = add_tuples(head,movement)
        diff_x, diff_y = (sub(*x) for x in zip(head,tail))
        tail_x, tail_y = tail
        if abs(diff_x) > 1 or abs(diff_y) > 1:
            if diff_y == 0:
                tail_x += sign(diff_x)
            elif diff_x == 0:
                tail_y += sign(diff_y)
            else:
                tail_x += sign(diff_x)
                tail_y += sign(diff_y)
        tail = (tail_x,tail_y)
        visited.add(tail)

print(len(visited))