with open("7.txt") as f:
    lines = [line.rstrip("\n") for line in f]

root = {}
cur_directory = None

for line in lines:
    if line.startswith("$"):
        command = line[2:].split(" ")
        program = command[0]
        if program != "cd":
            continue
        directory_name = command[1]
        if directory_name == "/":
            cur_directory = root
            continue
        directory = cur_directory[directory_name]
        if directory_name != "..":
            directory[".."] = cur_directory
        cur_directory = directory
    else:
        ident, name = line.split(" ")
        if ident == "dir":
            if name in cur_directory:
                continue
            cur_directory[name] = {}
        else:
            cur_directory[name] = int(ident)

def print_directory(directory,level=0):
    indent = " "*level*2
    for name, value in directory.items():
        if name == "..":
            continue
        if type(value) == int:
            print(indent,name, value)
        else:
            print(indent, name, "dir")
            print_directory(value, level+1)

dir_sizes = {}
def get_dir_size(directory, dir_name="/"):
    size = 0
    for name, value in directory.items():
        if name == "..":
            continue
        if type(value) == int:
            size += value
        else:
            size += get_dir_size(value,dir_name+name+"/")
    dir_sizes[dir_name] = size
    return size

get_dir_size(root)

ans = 0
for dir, size in dir_sizes.items():
    if size <= 100000:
        ans += size

print(ans)