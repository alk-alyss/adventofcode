from math import *

numbers = []
with open("input.txt", "r") as f:
	for line in f.readlines():
		numbers.append(list(line.strip()))

def magnitude(number):
	if isinstance(number, int):
		return number
	return 3*magnitude(number[0])+2*magnitude(number[1])

def printNumber(number):
	print(''.join(number))

number = ['[']
number += numbers.pop(0)
number.append(',')
number += numbers.pop(0)
number.append(']')

running = True
run = 0
while running:
	# if run == 1:
	# 	printNumber(number)
	depth = 0
	for i in range(len(number)):
		if depth == 5:
			nums = (int(number[i]),int(number[i+2]))

			for k in range(2):
				index = 1 if k%2 else -1
				index += i+k*2
				try:
					while not number[index].isdigit():
						index = index+1 if k%2 else index-1
						if index < 0: break
					else:
						num = str(int(number[index])+nums[k])
						number[index] = num
				except IndexError:
					continue

			number = number[:i-1]+["0"]+number[i+4:]
			# number.insert(i, '0')
			depth -=1
			break

		if number[i] == '[': depth+=1
		elif number[i] == ']': depth-=1

	else:
		for i in range(len(number)):
			if number[i].isdigit():
				num = int(number[i])
				if num > 9:
					num = num/2
					pair = ['[',str(floor(num)),',',str(ceil(num)),']']
					number = number[:i] + pair + number[i+1:]
					# number.insert(i+1, pair)
					break

		else:
			printNumber(number)
			# running = False
			if len(numbers) > 0:
				number.append(',')
				number += numbers.pop(0)
				number = ['['] + number + [']']
				# printNumber(number)
				run += 1
			else:
				running = False

number = ''.join(number)
print(magnitude(eval(number)))