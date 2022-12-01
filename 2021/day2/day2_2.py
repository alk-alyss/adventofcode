depth = 0
position = 0
aim = 0

with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.split()
		if line[0] == "forward":
			position += int(line[1])
			depth += aim * int(line[1])
		elif line[0] == "up":
			aim -= int(line[1])
		elif line[0] == "down":
			aim += int(line[1])

print(depth*position)