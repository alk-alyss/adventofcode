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

velocities = []
maxForce = 400
for i in range(-maxForce, maxForce+1):
	for j in range(-maxForce, maxForce+1):
		probe = [0, 0]
		velocity = [i, j]
		initialVelocity = velocity.copy()

		flag = False
		while probe[0] <= targetArea[1][0] and probe[1] >= targetArea[0][1]:
			probe, velocity = nextStep(probe, velocity)
			if isInTarget(probe):
				flag = True
				break
		
		if flag and initialVelocity not in velocities:
			velocities.append(initialVelocity)

print(len(velocities))