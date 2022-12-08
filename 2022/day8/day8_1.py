def searchNorth(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    while True:
        i -= 1
        if i < 0:
            break

        if grid[i][j] >= height:
            return False

    return True

def searchSouth(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    while True:
        i += 1
        if i >= len(grid):
            break

        if grid[i][j] >= height:
            return False

    return True

def searchEast(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    while True:
        j -= 1
        if j < 0:
            break

        if grid[i][j] >= height:
            return False

    return True

def searchWest(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    while True:
        j += 1
        if j >= len(grid[i]):
            break

        if grid[i][j] >= height:
            return False

    return True

grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append([int(x) for x in line.strip()])

result = len(grid)*2 + (len(grid)-2)*2
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):

        if searchNorth(grid, (i, j)) or searchSouth(grid, (i, j)) or searchEast(grid, (i, j)) or searchWest(grid, (i, j)):
            result += 1

print(result)
