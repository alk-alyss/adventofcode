nums = []
with open("input.txt", "r") as f:
	nums = f.readlines()

prevNum = nums[0] + nums[1] + nums[2]
result = 0
for i in range(len(nums)-2):
	num = nums[i] + nums[i+1] + nums[i+2]
	if num > prevNum:
		result += 1
	prevNum = num

print(result)
