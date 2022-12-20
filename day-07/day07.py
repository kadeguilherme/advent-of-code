import os
with open("day07.txt", "r") as file:
    data = file.read().strip().split("\n")

dirs = {}
directory_size = {}
sub_dir = []
totaldir = 0

for line in data:
    if line[0] == '$':
        ds, cmd, *dir = line.split()
        if cmd == 'cd':
            path = dir[0]
            if path == '/':
                curdir = path
            else:
                curdir = os.path.normpath((os.path.join(curdir, path)))
                # print(curdir)
            if curdir not in dirs:
                dirs[curdir] = []
                directory_size[curdir] = 0
    else:
        fsize, fname = line.split()
        if fsize != 'dir':
            directory_size[curdir] += int(fsize)

for ii in dirs:
    sub_dir.append(ii)

for ii in dirs:
    for i in directory_size:
        if i in ii and i != ii:
            size = directory_size[ii]
            directory_size[i] += size

for i in directory_size:
    if directory_size[i] <= 100000:
        totaldir += directory_size[i]

print(totaldir)
