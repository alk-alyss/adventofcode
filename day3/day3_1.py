pos = []
lines = 0
with open("input.txt", "r") as f:
	for line in f.readlines():
		lines += 1
		if pos == []:
			pos = [0 for i in range(len(line)-1)]
		
		for i in range(len(pos)):
			pos[i] += int(line[i])

gamma = ""
epsilon = ""
for i in range(len(pos)):
	gamma += str(1 if pos[i] > lines/2 else 0)
	epsilon += str(0 if pos[i] > lines/2 else 1)

gammarate = int(str(gamma), 2)
epsilonrate = int(str(epsilon), 2)
print(gammarate*epsilonrate)