grid = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()
		grid.append([int(x) for x in line])

minPoints = []
for y in range(len(grid)):
	for x in range(len(grid[y])):
		lowest = True
		for i in range(4):
			if not lowest:
				break
			if i==0:
				if y==0: continue
				lowest = grid[y][x] < grid[y-1][x]
			if i==1:
				if x==0: continue
				lowest = grid[y][x] < grid[y][x-1]
			if i==2:
				if y==len(grid)-1: continue
				lowest = grid[y][x] < grid[y+1][x]
			if i==3:
				if x==len(grid[y])-1: continue
				lowest = grid[y][x] < grid[y][x+1]
		if lowest:
			minPoints.append([y, x])

def basinSize(point):
	global grid
	checkGrid = grid.copy()

	queue = []
	queue.append([point[0],point[1]])

	size = 0
	while queue:
		p = queue.pop()
		if checkGrid[p[0]][p[1]] != 9:
			checkGrid[p[0]][p[1]] = 9
			size += 1
			if 0<=p[0]-1<=len(grid)-1 and 0<=p[1]<=len(grid[0])-1:
				queue.append([p[0]-1,p[1]])
			if 0<=p[0]+1<=len(grid)-1 and 0<=p[1]<=len(grid[0])-1:
				queue.append([p[0]+1,p[1]])
			if 0<=p[0]<=len(grid)-1 and 0<=p[1]-1<=len(grid[0])-1:
				queue.append([p[0],p[1]-1])
			if 0<=p[0]<=len(grid)-1 and 0<=p[1]+1<=len(grid[0])-1:
				queue.append([p[0],p[1]+1])
	
	return size


basins = []
for point in minPoints:
	basins.append(basinSize(point))

basins.sort(reverse=True)
print(basins)
print(basins[0]*basins[1]*basins[2])