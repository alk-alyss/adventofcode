def moveTail(head, tail):
    distX = head[0] - tail[0]
    distY = head[1] - tail[1]

    if abs(distX) <= 1 and abs(distY) <= 1:
        return

    # diagonals
    elif (distX > 1 and distY > 0) or (distY > 1 and distX > 0):
        tail[0] += 1
        tail[1] += 1
    elif (distX > 1 and distY < 0) or (distY < -1 and distX > 0):
        tail[0] += 1
        tail[1] -= 1
    elif (distX < -1 and distY > 0) or (distY > 1 and distX < 0):
        tail[0] -= 1
        tail[1] += 1
    elif (distX < -1 and distY < 0) or (distY < -1 and distX < 0):
        tail[0] -= 1
        tail[1] -= 1

    # straight
    elif distX > 1:
        tail[0] += 1
    elif distX < -1:
        tail[0] -= 1
    elif distY > 1:
        tail[1] += 1
    elif distY < -1:
        tail[1] -= 1

def printGrid(head, tail):
    for i in range(5, -1, -1):
        for j in range(6):
            if [j, i] == head:
                print('H', end='')
            elif [j, i] == tail:
                print('T', end='')
            else:
                print('.', end='')
        print()
    print('\n')


rope = [[0,0] for _ in range(10)]
head = rope[0]
tail = rope[-1]
tailPositions = set()

with open("input.txt", "r") as f:
    for line in f.readlines():
        dir, num = line.strip().split()

        for i in range(int(num)):
            match(dir):
                case "R":
                    head[0] += 1
                case "U":
                    head[1] += 1
                case "L":
                    head[0] -= 1
                case "D":
                    head[1] -= 1

            for j in range(9):
                moveTail(rope[j], rope[j+1])

            tailPositions.add(tuple(tail))

            # printGrid(head, tail)


print(len(tailPositions))
