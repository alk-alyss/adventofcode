from astar import astar

grid = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		grid.append([int(x) for x in line.strip()])

path = astar(grid, (0,0), (len(grid)-1,len(grid[0])-1))
if isinstance(path, str):
	print(path)
else:
	result = 0
	for pos in path[1:]:
		result += grid[pos[0]][pos[1]]

	print(result)
