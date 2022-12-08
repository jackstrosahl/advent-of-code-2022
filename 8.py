from itertools import repeat


map = []

with open("8-test.txt") as f:
    for line in f:
        line = line.rstrip("\n")
        map.append([int(height) for height in line])

def get_height(x,y):
    return map[y][x]

def all_shorter(height, xs,ys):
    if type(xs) == int:
        xs = repeat(xs,len(ys))
    elif type(ys) == int:
        ys = repeat(ys, len(xs))
    for x in xs:
        for y in ys:
            print(f"Checking {x,y}")
            if get_height(x,y) >= height:
                return False
    return True

width = len(map[0])
height = len(map)

ans = (width*2)+(height*2)-4
for x in range(1,width-1):
    for y in range(1,height-1):
        tree_height = get_height(x,y)
        print(f"Tree: {x,y}")
        if all_shorter(tree_height, range(x), y) \
        or all_shorter(tree_height, range(x+1,width), y) \
        or all_shorter(tree_height, x, range(y)) \
        or all_shorter(tree_height, x, range(y+1, height)):
            print("Visible")
            ans += 1

print(ans)