score = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        other, me = line.split()

        match(me):
            case "X":
                score += 1
            case "Y":
                score += 2
            case "Z":
                score += 3

        if (me == "X" and other == "A") or (me == "Y" and other == "B") or (me == "Z" and other == "C"):
            score += 3

        elif (me == "X" and other == "C") or (me == "Y" and other == "A") or (me == "Z" and other == "B"):
            score += 6

print(score)
