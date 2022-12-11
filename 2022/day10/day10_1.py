x = 1
cycles = 0

result = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()

        if line == "noop":
            cycles += 1

            if (cycles+20)%40 == 0:
                print(cycles, x, x*cycles)
                result += x*cycles

            continue

        v = int(line.split(' ')[1])

        cycles += 1

        if (cycles+20)%40 == 0:
            print(cycles, x, x*cycles)
            result += x*cycles

        cycles += 1

        if (cycles+20)%40 == 0:
            print(cycles, x, x*cycles)
            result += x*cycles

        x += v

print(result)
