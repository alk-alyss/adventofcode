with open("input.txt", "r") as f:
	result = 0
	for line in f.readlines():
		output = line.strip('\n').split(" | ")[1].split(" ")

		for item in output:
			if len(item) in [2, 3, 4, 7]:
				result += 1

print(result)