allDividers = 1
class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false

    def inspectItems(self):
        global monkeys

        i = 0
        while(len(self.items) > 0):
            i += 1
            item = self.items.pop(0)

            operation = self.operation.split()[1]
            operand = self.operation.split()[2]

            if operand == "old":
                operand = item
            else:
                operand = int(operand)

            match(operation):
                case '+':
                    item += operand
                case '-':
                    item -= operand
                case '*':
                    item *= operand
                case '/':
                    item /= operand

            item %= allDividers

            if item % self.test == 0:
                monkeys[self.true].getItem(item)
                # print(f"throw to monkey {self.true}")
            else:
                monkeys[self.false].getItem(item)
                # print(f"throw to monkey {self.false}")

        return i


    def getItem(self, item):
        self.items.append(item)

    def __str__(self):
        return str(self.items)

monkeys = []
with open("input.txt", "r") as f:
    text = f.read()

    text = text.strip().split('\n\n')

    for t in text:
        t = t.split('\n')

        items = list(map(int, t[1].split(':')[1].strip().split(", ")))

        operation = t[2].split(':')[1].strip().split('=')[1].strip()

        test = int(t[3].split(':')[1].strip().split()[-1])
        allDividers *= test

        true = int(t[4].split(':')[1].strip().split()[-1])
        false = int(t[5].split(':')[1].strip().split()[-1])

        monkeys.append(Monkey(items, operation, test, true, false))

result = [0 for _ in range(len(monkeys))]
for i in range(10000):
    for j, monkey in enumerate(monkeys):
        result[j] += monkey.inspectItems()

result.sort(reverse=True)
print(result[0] * result[1])
