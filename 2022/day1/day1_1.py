maxCalories = 0

with open("input.txt", "r") as f:
    calories = 0
    for line in f.readlines():
        line = line.strip()

        if line == "":
            maxCalories = max(maxCalories, calories)
            calories = 0
            continue

        calories += int(line)

print(maxCalories)
