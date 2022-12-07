import string

def getParent(dir):
    dirs = dir.split('/')
    dirs = dirs[:-1]
    if len(dirs) == 1:
        return '/'

    return '/'.join(dirs)

def childDir(parent, dir):
    if parent == "/":
        parent += dir
    else:
        parent += '/' + dir

    return parent

def getSize(dir):
    global dirs

    size = 0
    for item in dirs[dir]:
        try:
            size += int(item)
        except Exception:
            size += getSize(item)

    return size

dirs = {}
currentDir = ""

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line[0] == "$":
            command = line[1:].split()

            if command[0] == "cd":
                dirName = command[1]
                if dirName == "/":
                    currentDir += dirName
                elif dirName == "..":
                    currentDir = getParent(currentDir)
                else:
                    currentDir = childDir(currentDir, dirName)

                if currentDir not in dirs.keys():
                    dirs[currentDir] = []

        else:
            output = line.split()

            if output[0] == "dir":
                dirs[currentDir].append(childDir(currentDir, output[1]))

            else:
                dirs[currentDir].append(output[0])

sizes = {}
for dir in dirs.keys():
    sizes[dir] = getSize(dir)

result = 0
for size in sizes.values():
    if size <= 100000:
        result += size

print(result)
