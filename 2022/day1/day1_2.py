maxCalories = [0]

with open("input.txt", "r") as f:
    calories = 0
    for line in f.readlines():
        line = line.strip()

        if line == "":
            for i in range(len(maxCalories)):
                if calories > maxCalories[i]:
                    maxCalories.insert(i, calories)
                    break
            calories = 0
            continue

        calories += int(line)

calories = sum(maxCalories[0:3])

print(calories)
