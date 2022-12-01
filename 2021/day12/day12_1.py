nodes = {}
with open("example.txt", "r") as f:
	for line in f.readlines():
		start, end = line.strip().split("-")

		if start not in nodes:
			nodes[start] = [end]
		else:
			nodes[start].append(end)
		
		if end not in nodes:
			nodes[end] = [start]
		else:
			nodes[end].append(start)

path = ["start"]