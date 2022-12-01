with open("input.txt", "r") as f:
	grid = []
	for line in f.readlines():
		grid.append([int(x) for x in line.strip()])

def nextStep(grid: list):
	res = 0
	nextGrid = [[x for x in line] for line in grid]
	
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			nextGrid[i][j] = grid[i][j]+1

	while any([x>9 for line in nextGrid for x in line]):
		for i in range(len(nextGrid)):
			for j in range(len(nextGrid[i])):
				if nextGrid[i][j] > 9:
					res += 1
					for k in range(-1, 2):
						for l in range(-1, 2):
							if k == 0 and l == 0: continue
							if i+k < 0 or j+l < 0: continue
							try:
								if nextGrid[i+k][j+l] == 0: continue
								nextGrid[i+k][j+l] += 1
							except:
								continue
					nextGrid[i][j] = 0
	
	return res, nextGrid

result = 0
for i in range(100):
	temp, grid = nextStep(grid)
	result += temp

print(result)
