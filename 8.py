from itertools import repeat


map = []

with open("8.txt") as f:
    for line in f:
        line = line.rstrip("\n")
        map.append([int(height) for height in line])

def get_height(x,y):
    return map[y][x]

def all_shorter(height,xs,ys):
    if type(xs) == int:
        xs = [xs]
    elif type(ys) == int:
        ys = [ys]
    for x in xs:
        for y in ys:
            if get_height(x,y) >= height:
                return False
    return True

width = len(map[0])
height = len(map)

ans = (width*2)+(height*2)-4
for x in range(1,width-1):
    for y in range(1,height-1):
        tree_height = get_height(x,y)
        if all_shorter(tree_height, range(x), y) \
        or all_shorter(tree_height, range(x+1,width), y) \
        or all_shorter(tree_height, x, range(y)) \
        or all_shorter(tree_height, x, range(y+1, height)):
            ans += 1

print(ans)