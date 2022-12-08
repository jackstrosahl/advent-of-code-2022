from functools import reduce
from operator import mul


map = []

with open("8.txt") as f:
    for line in f:
        line = line.rstrip("\n")
        map.append([int(height) for height in line])

def get_height(x,y):
    return map[y][x]

def tree_view(height,xs,ys):
    if type(xs) == int:
        xs = [xs]
    elif type(ys) == int:
        ys = [ys]
    
    view_dist = 0
    for x in xs:
        for y in ys:
            view_dist += 1
            if get_height(x,y) >= height:
                return False, view_dist
    return True, view_dist

width = len(map[0])
height = len(map)

ans_p1 = (width*2)+(height*2)-4
ans_p2 = 0
for x in range(1,width-1):
    for y in range(1,height-1):
        tree_height = get_height(x,y)
        shorter_trees, view_dists = zip( \
            tree_view(tree_height, range(x-1,-1,-1), y), \
            tree_view(tree_height, range(x+1,width), y), \
            tree_view(tree_height, x, range(y-1,-1,-1)), \
            tree_view(tree_height, x, range(y+1, height)))
        if any(shorter_trees):
            ans_p1 += 1
        scenic_score = reduce(mul, view_dists)
        if scenic_score > ans_p2:
            ans_p2 = scenic_score

print(ans_p1)
print(ans_p2)