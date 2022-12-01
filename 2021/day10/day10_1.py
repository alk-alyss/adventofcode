points = {")":3, "]":57, "}":1197, ">":25137}
opening = ["(", "[", "{", "<"]
closing = [")", "]", "}", ">"]

def bracketMatch(line):
	stack = []
	for char in line:
		if char in opening:
			stack.append(char)
		elif char in closing:
			if stack[-1] == opening[closing.index(char)]:
				stack.pop()
			else:
				return points.get(char)
	
	return 0

	

with open("input.txt", "r") as f:
	result = 0
	for line in f.readlines():
		result += bracketMatch(line)

print(result)