grid = {}

with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip().split()
		state = True if line[0]=="on" else False
		coords = line[1].split(',')
		xRange = list(map(int, coords[0].lstrip("x=").split("..")))
		yRange = list(map(int, coords[1].lstrip("y=").split("..")))
		zRange = list(map(int, coords[2].lstrip("z=").split("..")))
		if not -50<=xRange[0]<=50 or not -50<=xRange[1]<=50: break
		if not -50<=yRange[0]<=50 or not -50<=yRange[1]<=50: break
		if not -50<=zRange[0]<=50 or not -50<=zRange[1]<=50: break
		for x in range(xRange[0], xRange[1]+1):
			for y in range(yRange[0], yRange[1]+1):
				for z in range(zRange[0], zRange[1]+1):
					coord = (x,y,z)
					grid[coord] = state

count = 0
for g in grid.values():
	count += 1 if g else 0
print(count)