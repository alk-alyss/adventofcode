x = 1
cycles = 0

def crt():
    global x, cycles

    charToPrint = '#' if abs((cycles-1)%40-x) < 2 else '.'
    print(charToPrint, end='')
    if cycles%40 == 0: print()

with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()

        if line == "noop":
            cycles += 1
            crt()

        else:
            v = int(line.split(' ')[1])

            cycles += 1
            crt()

            cycles += 1
            crt()

            x += v
