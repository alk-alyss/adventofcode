image = {}
with open("input.txt", "r") as f:
	algo = [x=='#' for x in f.readline().strip()]
	f.readline()
	lines = [line.strip() for line in f.readlines()]
	r = len(lines)
	c = len(lines[0])
	for i in range(r):
		for j in range(c):
			if lines[i][j]=='#':
				image[(i,j)] = True
			else:
				image[(i, j)] = False


def getIndex(image, i, j):
	global oB
	index = ''
	for k in range(-1, 2):
		for l in range(-1, 2):
			spot = (i+k, j+l)
			try:
				index += '1' if image[spot] else '0'
			except KeyError:
				index += '1' if oB else '0'
	
	return int(index, 2)

offset = 1
startR = 0
endR = r
startC = 0
endC = c
oB = False
for step in range(50):
	r += (2*offset)
	c += (2*offset)
	startR -= offset
	endR += offset
	startC -= offset
	endC += offset

	newImage = {}
	for i in range(startR, endR):
		for j in range(startC, endC):
			newImage[(i,j)]=algo[getIndex(image, i, j)]
	
	image = newImage

	oB = algo[-1] if oB else algo[0]

res = 0
for i in range(startR, endR):
	for j in range(startC, endC):
		res += 1 if image[(i,j)] else 0

print(res)