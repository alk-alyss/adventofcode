def sumOfDigitsFrom1ToN(n):
	result = 0
	for i in range(0,n):
		result += i+1
	return result

with open("input.txt", "r") as f:
	numbers = list(map(int, f.readline().split(',')))

minFuel = -1
pos = 0
for i in range(max(numbers)):
	fuel = 0
	for number in numbers:
		fuel += sumOfDigitsFrom1ToN(abs(i-number))

	if minFuel == -1:
		minFuel = fuel
		pos = i
	elif minFuel>=fuel:
		minFuel = fuel
		pos = i

print(minFuel, pos)
