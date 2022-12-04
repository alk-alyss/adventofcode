result = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        first, second = line.split(',')

        firstStart, firstEnd = list(map(int, first.split('-')))
        secondStart, secondEnd = list(map(int, second.split('-')))

        condition1 = (firstStart <= secondStart and firstEnd >= secondStart)
        condition2 = (firstStart <= secondEnd and firstEnd >= secondEnd)
        condition3 = (secondStart <= firstStart and secondEnd >= firstStart)
        condition4 = (secondStart <= firstEnd and secondEnd >= firstEnd)


        if condition1 or condition2 or condition3 or condition4:
            result += 1

print(result)
