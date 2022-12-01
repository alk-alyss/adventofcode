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
			minPoints.append(grid[y][x])

result = 0
for point in minPoints:
	result += point+1

print(result)
