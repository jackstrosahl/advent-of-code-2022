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

def get_visited(length):
    rope = [(0,0) for _ in range(length)]

    visited = set()

    for direction, distance in moves:
        movement = movements[direction]
        for i in range(distance):
            rope[0] = add_tuples(rope[0],movement)
            for i in range(1,length):
                prev_knot, cur_knot = rope[i-1:i+1]
                diff_x, diff_y = (sub(*x) for x in zip(prev_knot,cur_knot))
                tail_x, tail_y = cur_knot
                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    if diff_y == 0:
                        tail_x += sign(diff_x)
                    elif diff_x == 0:
                        tail_y += sign(diff_y)
                    else:
                        tail_x += sign(diff_x)
                        tail_y += sign(diff_y)
                rope[i] = (tail_x,tail_y)
            visited.add(rope[-1])
    
    return len(visited)

print(get_visited(2))
print(get_visited(10))