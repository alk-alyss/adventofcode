nums = []
with open("input.txt", "r") as f:
	nums = list(map(int, f.readlines()))

prevNum = nums[0]
result = 0
for i in nums:
	if i > prevNum:
		result += 1
	prevNum = i

print(result)
