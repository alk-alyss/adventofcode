with open("input.txt", "r") as f:
	line = f.readline()
	x, y = line.lstrip("target area: ").split(", ")
	x = list(map(int, x.lstrip("x=").split("..")))
	y = list(map(int, y.lstrip("y=").split("..")))

targetArea = [[min(x), min(y)], [max(x), max(y)]]

def nextStep(probe, velocity):
	probe[0] += velocity[0]
	probe[1] += velocity[1]

	if velocity[0] != 0:
		dvx = -1 if velocity[0]>0 else 1
		velocity[0] += dvx

	velocity[1] -= 1

	return probe, velocity

def isInTarget(probe):
	if targetArea[0][0] <= probe[0] <= targetArea[1][0] and targetArea[0][1] <= probe[1] <= targetArea[1][1]:
		return True
	else: return False

totalMaxY = 0
maxForce = 150
for i in range(1, maxForce+1):
	for j in range(1, maxForce+1):
		probe = [0, 0]
		velocity = [i, j]

		flag = False
		maxY = 0
		while probe[0] <= targetArea[1][0] and probe[1] >= targetArea[0][1]:
			probe, velocity = nextStep(probe, velocity)
			maxY = max(maxY, probe[1])
			flag |= isInTarget(probe)
		
		if flag:
			totalMaxY = max(totalMaxY, maxY)

print(totalMaxY)