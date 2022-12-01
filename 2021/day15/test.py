def shiftLine(line, n):
    v = ['1','2','3','4','5','6','7','8','9']
    return "".join([v[(v.index(i)+n)%9] for i in list(line)])

def increaseMap(riskmap):
    newRiskmap = []
    ylen = len(riskmap)
    for y in range(ylen * 5):
        newRiskmap.append(
            shiftLine(riskmap[y % ylen], y//ylen + 0) +
            shiftLine(riskmap[y % ylen], y//ylen + 1) +
            shiftLine(riskmap[y % ylen], y//ylen + 2) +
            shiftLine(riskmap[y % ylen], y//ylen + 3) +
            shiftLine(riskmap[y % ylen], y//ylen + 4)
            )
    return newRiskmap

def calcCosts(enlarge):
    riskmap = open('input.txt','r').read().split('\n')[:-1]
    costsToLocation = {(0,0): 0}
    if (enlarge):
        riskmap = increaseMap(riskmap)
    
    while True:
        costs = -1
        somethingChanged = False
        print(f'{len(costsToLocation)} / {len(riskmap[0]) * len(riskmap)} = {round(len(costsToLocation) / (len(riskmap[0]) * len(riskmap)) * 100,2)} % discovered')
        for k,v in list(costsToLocation.items()):
            x,y = k
            if (x == len(riskmap[0])-1 and y == len(riskmap)-1):
                costs = v
            for xx,yy in [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]:
                if (-1 < xx < len(riskmap[0]) and -1 < yy < len(riskmap)):
                    if not (xx,yy) in costsToLocation:
                        costsToLocation[(xx,yy)] = v + int(riskmap[yy][xx])
                        somethingChanged = True
                    elif costsToLocation[(xx,yy)] > v + int(riskmap[yy][xx]):
                        costsToLocation[(xx,yy)] = v + int(riskmap[yy][xx])
                        somethingChanged = True
        if not somethingChanged:
            break
    return costs

print("Part 1:",calcCosts(False))
print("Part 2:",calcCosts(True))