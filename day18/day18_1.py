import math

def parseLine(line):
	return line[1:-1]

numbers = []
with open("example.txt", "r") as f:
	for line in f.readlines():
		numbers.append(parseLine(line.strip()))

def split(num):
	num = num/2
	return [math.floor(num), math.ceil(num)]

def explode(number):
	pass

def magnitude(number):
	if isinstance(number, int): return number
	else: return 3*number[0]+2*number[1]


print(numbers)