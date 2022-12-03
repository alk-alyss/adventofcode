import string

def getpriority(ch):
    if ch in string.ascii_lowercase:
        return ord(ch)-96

    return ord(ch)-64+26


result = 0

with open("input.txt", "r") as f:
    for line in f.readlines():
        line.strip()
        first = line[:int(len(line)/2)]
        second = line[int(len(line)/2):]

        for c in first:
            if c in second:
                p = getpriority(c)
                # print(c, p)
                result += p
                break

print(result)
