result = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        first, second = line.split(',')

        firstStart, firstEnd = list(map(int, first.split('-')))
        secondStart, secondEnd = list(map(int, second.split('-')))

        condition1 = (firstStart <= secondStart and firstEnd >= secondEnd)
        condition2 = (secondStart <= firstStart and secondEnd >= firstEnd)


        if condition1 or condition2:
            result += 1

print(result)
