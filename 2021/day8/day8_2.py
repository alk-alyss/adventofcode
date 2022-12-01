with open("input.txt", "r") as f:
	lines = []
	for line in f.readlines():
		pattern, output = line.strip('\n').split(" | ")
		pattern = pattern.split(' ')
		output = output.split(' ')
		lines.append([pattern, output])

def getUpperLeft(segments):
	if segments[3] and segments[9]:
		return (segments[9]-segments[3]).pop()
	else:
		raise IndexError

def getMiddle(segments):
	if segments[4] and segments[1]:
		try:
			upperLeft = getUpperLeft(segments)
			compareSet = segments[1].copy()
			compareSet.add(upperLeft)
			return (segments[4]-compareSet).pop()
		except IndexError:
			raise IndexError

	else:
		raise IndexError

def solve(line):
	segments = [set() for i in range(10)]
	pattern = line[0]
	output = line[1]

	while set() in segments:
		for p in pattern:
			p = set(p)
			if p in segments:
				continue
			try:
				if len(p) == 2:
					segments[1] = p
				elif len(p) == 3:
					segments[7] = p
				elif len(p) == 4:
					segments[4] = p
				elif len(p) == 7:
					segments[8] = p
				elif len(p) == 6:
					if segments[4] and segments[4].issubset(p):
						segments[9] = p
					elif getMiddle(segments) in p:
						segments[6] = p
					else:
						segments[0] = p
				elif len(p) == 5:
					if segments[7] and segments[7].issubset(p):
						segments[3] = p
					elif getUpperLeft(segments) in p:
						segments[5] = p
					else:
						segments[2] = p
			except IndexError:
				continue

	res = ''
	for o in output:
		o = set(o)
		res += str(segments.index(o))
	return int(res)

result = 0
for line in lines:
	result += solve(line)

print(result)
