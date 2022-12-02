score = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        other, me = line.split()

        if me == "X":
            match(other):
                case "A":
                    score += 3
                case "B":
                    score += 1
                case "C":
                    score += 2
        elif me == "Y":
            score += 3
            match(other):
                case "A":
                    score += 1
                case "B":
                    score += 2
                case "C":
                    score += 3
        else:
            score += 6
            match(other):
                case "A":
                    score += 2
                case "B":
                    score += 3
                case "C":
                    score += 1


print(score)
