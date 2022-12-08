def searchNorth(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    result = 1
    while True:
        i -= 1
        if i <= 0 or grid[i][j] >= height:
            break

        result += 1

    return result

def searchSouth(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    result = 1
    while True:
        i += 1
        if i >=len(grid)-1 or grid[i][j] >= height:
            break

        result += 1

    return result

def searchEast(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    result = 1
    while True:
        j -= 1
        if j <= 0 or grid[i][j] >= height:
            break

        result += 1

    return result

def searchWest(grid, startPos):
    i, j = startPos
    height = grid[i][j]

    result = 1
    while True:
        j += 1
        if j >= len(grid[i])-1 or grid[i][j] >= height:
            break

        result += 1

    return result

grid = []
with open("input.txt", "r") as f:
    for line in f.readlines():
        grid.append([int(x) for x in line.strip()])

maxResult = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):

        result = 1
        result *= searchNorth(grid, (i,j))
        result *= searchSouth(grid, (i,j))
        result *= searchEast(grid, (i,j))
        result *= searchWest(grid, (i,j))

        maxResult = max(maxResult, result)

print(maxResult)
