with open("input.txt", "r") as f:
	fish = list(map(int, f.readline().split(",")))

for day in range(256):
	for i in range(len(fish)):
		if fish[i]==0:
			fish.append(8)
			fish[i] = 6
		else:
			fish[i] -= 1

print(len(fish))
