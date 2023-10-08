from collections import defaultdict

def printObjects(objects):
    for y in range(10):
        for x in range(494, 504):
            char = '.'
            match(objects[(x,y)]):
                case 1: char = '#'
                case 2: char = 'o'

            print(char, end="")
        print()

objects = defaultdict(int)
source = (500, 0)
maxDepth = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        points = [tuple(map(int, x.strip().split(','))) for x in line.split("->")]

        for i in range(len(points)-1):
            start, end = sorted([points[i], points[i+1]])

            for x in range(abs(start[0]-end[0])+1):
                for y in range(abs(start[1]-end[1])+1):
                    point = (start[0]+x, start[1]+y)
                    maxDepth = max(maxDepth, point[1])

                    objects[point] = 1

def simulateSand(objects):
    sand = source

    for _ in range(maxDepth):
        moves = [(0, 1), (-1, 1), (1, 1)]

        for move in moves:
            newPoint = (sand[0]+move[0], sand[1]+move[1])

            if not objects[newPoint]:
                sand = newPoint
                break
        else:
            objects[sand] = 2
            return True

    return False

steps = 0
while True:
    # printObjects(objects)
    if not simulateSand(objects):
        break
    steps += 1

print(steps)
