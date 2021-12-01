text = []
with open("input.txt", "r") as f:
	text = f.readlines()

prevNum = int(text[0]) + int(text[1]) + int(text[2])
result = 0
for i in range(len(text)-2):
	num = int(text[i]) + int(text[i+1]) + int(text[i+2])
	if num > prevNum:
		result += 1
	prevNum = num

print(result)
