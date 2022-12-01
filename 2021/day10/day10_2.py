points = {")":1, "]":2, "}":3, ">":4}
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
				return 0
	
	stack.reverse()
	result = 0
	for char in stack:
		result *= 5
		result += points.get(closing[opening.index(char)])
	
	return result

		

with open("input.txt", "r") as f:
	results = []
	for line in f.readlines():
		result = bracketMatch(line) 
		if result != 0:
			results.append(result)

results.sort()
print(results[len(results)//2])