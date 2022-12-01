lines = []
with open("input.txt") as f:
	for line in f.readlines():
		line = line.strip('\n')
		lines.append(line)

oxy = lines.copy()
co2 = lines.copy()

for i in range(len(lines[0])):
	ones = 0
	zeros = 0
	for line in oxy:
		if line[i] == "1":
			ones += 1
		else:
			zeros += 1
	obit = 1 if ones>=zeros else 0

	ones = 0
	zeros = 0
	for line in co2:
		if line[i] == "1":
			ones += 1
		else:
			zeros += 1
	cbit = 0 if zeros<=ones else 1

	o = 0
	while len(oxy) > 1:
		if o >= len(oxy):
			break
		if int(oxy[o][i]) == obit:
			o += 1
		else:
			oxy.pop(o)

	c = 0
	while len(co2) > 1:
		if c >= len(co2):
			break
		else:
			if int(co2[c][i]) == cbit:
				c += 1
			else:
				co2.pop(c)

oxydeci = int(oxy.pop(), 2)
co2deci = int(co2.pop(), 2)

print(oxydeci*co2deci)
