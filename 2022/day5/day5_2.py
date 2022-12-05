data = []
instructions = []

with open("input.txt", "r") as f:
    while(True):
        line = f.readline()

        if line == "\n":
            break

        data.append(line)

    for line in f.readlines():
        instructions.append(line.strip())

data.reverse()
data[0] = data[0].split()

stacks = [[] for _ in range(len(data[0]))]

for d in data[1:]:
    for i in range(0, len(d), 4):
        box = d[i:i+3]
        if ' ' not in box:
            stacks[int(i/4)].append(box[1])

for instruction in instructions:
    instruction = instruction.split(' ')
    num = int(instruction[1])
    src = int(instruction[3])-1
    dest = int(instruction[5])-1

    for i in range(num):
        stacks[dest].append(stacks[src].pop())

for s in stacks:
    print(s[-1], end='')
