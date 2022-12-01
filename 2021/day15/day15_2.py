from astar import astar

grid = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		grid.append([int(x) for x in line.strip()])

fullGridRow = []
for i in range(len(grid)):
	line = grid[i]
	fullGridRow.append(line)
	for j in range(4):
		newLine = []
		for x in line:
			x += 1
			if x > 9:
				x = 1
			newLine.append(x)
		line = newLine
		fullGridRow[i] += line

fullGrid = []
for i in range(5):
	fullGrid += [[x for x in line] for line in fullGridRow]
	for j in range(len(fullGridRow)):
		for k in range(len(fullGridRow[j])):
			fullGridRow[j][k] += 1
			if fullGridRow[j][k] > 9:
				fullGridRow[j][k] = 1

path = astar(fullGrid, (0,0), (len(fullGrid)-1,len(fullGrid[0])-1))
if isinstance(path, str):
	print(path)
else:
	result = 0
	for pos in path[1:]:
		result += fullGrid[pos[0]][pos[1]]

	print(result)
