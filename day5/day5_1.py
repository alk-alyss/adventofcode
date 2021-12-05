lines = []
maxX = 0
maxY = 0
with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip('\n').split(" -> ")
		start = list(map(int, line[0].split(',')))
		end = list(map(int, line[1].split(',')))
		maxX = max(maxX, max(start[0], end[0]))
		maxY = max(maxY, max(start[1], end[1]))
		lines.append([start,end])

grid = [[0 for x in range(maxX+1)] for y in range(maxY+1) ]

for line in lines:
	start = line[0]
	end = line[1]
	lineXDiff = end[0] - start[0]
	lineYDiff = end[1] - start[1]

	if lineYDiff == 0:
		for i in range(abs(lineXDiff)+1):
			offset = i if lineXDiff>0 else -i
			grid[start[1]][start[0]+offset] += 1
	elif lineXDiff == 0:
		for i in range(abs(lineYDiff)+1):
			offset = i if lineYDiff>0 else -i
			grid[start[1]+offset][start[0]] += 1

result = 0
for line in grid:
	# print(line)
	for pos in line:
		if pos > 1:
			result += 1

print(result)
