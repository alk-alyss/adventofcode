from collections import defaultdict as dd
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

pairs = dd(int)
for i in range(len(polymer)-1):
	pair = polymer[i:i+2]
	pairs[pair] += 1

for step in range(40):
	nextPairs = dd(int)
	for pair in pairs.keys():
		newChar = rules[pair]

		newPairs = [pair[0]+newChar, newChar+pair[1]]
		for newPair in newPairs:
			nextPairs[newPair] += pairs[pair]

	pairs = nextPairs
		
chars = dd(int)
for pair in pairs.keys():
	for char in pair:
		chars[char] += pairs[pair]

chars[polymer[0]] += 1
chars[polymer[-1]] += 1

maxCharCount = max(chars.values())/2
minCharCount = min(chars.values())/2
print(int(maxCharCount-minCharCount))