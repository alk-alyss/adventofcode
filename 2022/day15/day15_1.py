sensors = []
beacons = []
with open("example.txt", "r") as f:
    for line in f.readlines():
        sensorInput, beaconInput = line.strip().split(':')

        sensorInput = sensorInput.strip("Sensor at").split(",")
        sensor = [int(x.split('=')[1]) for x in sensorInput]
        sensors.append(tuple(sensor))

        beaconInput = beaconInput.strip("closest beacon is at").split(",")
        beacon = [int(x.split('=')[1]) for x in beaconInput]
        beacons.append(tuple(beacon))

for y in range(26):
    for x in range(26):
        point = (x, y)

        if point in sensors:
            print('S', end='')
            continue

        if point in beacons:
            print('B', end='')
            continue

        print('.', end='')

    print()
