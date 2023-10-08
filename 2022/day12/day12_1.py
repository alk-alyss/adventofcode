def findPath(pos, grid, end, visited=[]):
    visited.append(pos)

    possibleMoves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in possibleMoves:
        newPos = (pos[0]+move[0], pos[1]+move[1])

        try:
            if abs(grid[newPos[1]][newPos[0]] - grid[pos[1]][pos[0]]) > 1:
                continue

            if newPos == end:
                return [newPos]

            if newPos not in visited:
                result = findPath(newPos, grid, end, visited)
                if result is not None:
                    result.append(newPos)
                    return result

        except IndexError:
            continue

    return None

grid = []
start = ()
end = ()
with open("example.txt", "r") as f:
    for i, line in enumerate(f.readlines()):
        row = []
        for j, x in enumerate(line.strip()):
            if x == 'S':
                row.append(0)
                start = (j, i)
            elif x == 'E':
                row.append(25)
                end = (j, i)
            else:
                row.append(ord(x) - ord('a'))

        grid.append(row)

path = findPath(start, grid, end, [])
path.reverse()
for p in path:
    print(p)
