grid = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		grid.append([x for x in line.strip()])

def printGrid(grid):
	for line in grid:
		print(line)
	print()

def step(grid):
	global somethingChanged
	newGrid = [['.' for y in range(len(grid[x]))] for x in range(len(grid))]
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			try:
				if grid[i][j]==">":
					if grid[i][j+1]==".":
						newGrid[i][j+1] = ">"
						somethingChanged = True
					else:
						newGrid[i][j] = ">"
				elif grid[i][j]=="v":
					newGrid[i][j] = "v"
			except IndexError:
				if grid[i][0]=='.':
					newGrid[i][0] = ">"
					somethingChanged = True
				else:
					newGrid[i][j] = ">"
	grid = newGrid

	newGrid = [['.' for y in range(len(grid[x]))] for x in range(len(grid))]
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			try:
				if grid[i][j]=="v":
					if grid[i+1][j]==".":
						newGrid[i+1][j] = "v"
						somethingChanged = True
					else:
						newGrid[i][j] = "v"
				elif grid[i][j]==">":
					newGrid[i][j] = ">"
			except IndexError:
				if grid[0][j]=='.':
					newGrid[0][j] = "v"
					somethingChanged = True
				else:
					newGrid[i][j] = "v"
	grid = newGrid

	return grid

i = 0
while True:
	somethingChanged = False
	grid = step(grid)
	i+=1
	# printGrid(grid)
	if not somethingChanged:
		break

print(i)