def comparePackets(packet1, packet2):
    if type(packet1) is int and type(packet2) is int:
        if packet1 < packet2:
            return 2
        if packet1 == packet2:
            return 1

        return 0

    if type(packet1) is int:
        newPacket = [[packet1], packet2]
        return comparePackets(newPacket[0], newPacket[1])

    if type(packet2) is int:
        newPacket = [packet1, [packet2]]
        return comparePackets(newPacket[0], newPacket[1])

    if type(packet1) is list and type(packet2) is list:
        result = 0
        while True:
            if len(packet1) == 0 and len(packet2) > 0:
                return 2
            if len(packet1) > 0 and len(packet2) == 0:
                return 0
            if len(packet1) == 0 and len(packet2) == 0:
                return 1

            newPacket = [packet1.pop(0), packet2.pop(0)]
            result = comparePackets(newPacket[0], newPacket[1])

            if result == 2:
                return 2
            if result == 0:
                return 0

    return 0

packets = []
with open("example.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()

        if line == "":
            continue

        packets.append(eval(line))

result = 0
for i in range(0, len(packets), 2):
    if comparePackets(packets[i], packets[i+1]) > 0:
        index = i//2 + 1
        print(index)
        result += index

print(result)
