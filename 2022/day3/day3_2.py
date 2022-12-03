import string

def getpriority(ch):
    if ch in string.ascii_lowercase:
        return ord(ch)-96

    return ord(ch)-64+26


result = 0

with open("input.txt", "r") as f:
    while(True):
        group = [f.readline() for _ in range(3)]

        if "" in group:
            break

        for c in group[0]:
            if c in group[1] and c in group[2]:
                print(c)
                result += getpriority(c)
                break

print(result)
