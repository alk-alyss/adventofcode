text = []
with open("input.txt", "r") as f:
	text = f.readlines()

prevNum = int(text[0])
result = 0
for i in text:
	i = int(i)
	if i > prevNum:
		result += 1
	prevNum = i

print(result)
