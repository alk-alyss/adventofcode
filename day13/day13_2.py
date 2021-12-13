folds = []
dots = []

with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()
		if line == '': continue
		elif "fold" in line:
			line = line.lstrip("fold along ").split('=')
			line[1] = int(line[1])
			folds.append(line)
		else:
			dots.append(list(map(int, line.split(','))))

xLen = max(dots, key=lambda x: x[0])[0]+1
xLen = xLen if xLen%2 else xLen+1

yLen = max(dots, key=lambda x: x[1])[1]+1
yLen = yLen if yLen%2 else yLen+1

grid = [[0 for x in range(xLen)] for y in range(yLen)]
for dot in dots:
	x = dot[0]
	y = dot[1]
	grid[y][x] = 1

for fold in folds:
	if fold[0] == 'y':
		foldGrid = grid[fold[1]+1:]
		grid = grid[:fold[1]]

		for i in range(len(foldGrid)):
			grid[-1-i] = [grid[-1-i][j] or foldGrid[i][j] for j in range(len(foldGrid[i]))]

	elif fold[0] == 'x':
		foldGrid = [line[fold[1]+1:] for line in grid]
		grid = [line[:fold[1]] for line in grid]
		
		for i in range(len(foldGrid)):
			grid[i] = [grid[i][-1-j] or foldGrid[i][j] for j in range(len(foldGrid[i]))][::-1]

for line in grid:
	for x in line:
		c = "#" if x else " "
		print(c, end='')
	print()