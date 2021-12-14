rules = {}
with open("input.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()
		if line == '': continue
		elif "->" in line:
			line = line.split(" -> ")
			rules[line[0]] = line[1]
		else:
			polymer = line

for step in range(10):
	newPolymer = ""
	for i in range(len(polymer)-1):
		newPolymer += polymer[i]
		newPolymer += rules[polymer[i]+polymer[i+1]]
	newPolymer += polymer[-1]

	polymer = newPolymer

chars = set(polymer)
maxCharCount = 0
minCharCount = 10**10
for char in chars:
	maxCharCount = max(maxCharCount, polymer.count(char))
	minCharCount = min(minCharCount, polymer.count(char))

print(maxCharCount-minCharCount)