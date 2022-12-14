import os
with open("day07.txt", "r") as file:
    data = file.read().strip().split("\n")

dirs = {}
directory_size = {}

for line in data:
    if line[0] == '$':
        ds, cmd, *dir = line.split()
        if cmd == 'cd':
            path = dir[0]
            if path == '/':
                curdir = path
            else:
                #print(os.path.join(curdir, path))
                curdir = os.path.normpath((os.path.join(curdir, path)))
                # print(curdir)
            if curdir not in dirs:
                dirs[curdir] = []
    else:
        print(line.split())
print(dirs)
