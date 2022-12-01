boards = []
with open("input.txt", "r") as f:
	numbers = f.readline().strip('\n').split(',')
	f.readline()

	board = []
	for line in f.readlines():
		if line in ["", "\n"]:
			boards.append(board)
			board = []
			continue

		line = line.strip('\n').split(' ')
		for item in line:
			if item == '':
				line.remove(item)
		board.append(line)
	
	boards.append(board)

def findWinningBoard(boards):
	markedSpots = [[] for i in range(len(boards))]
	for number in numbers:
		for i in range(len(boards)):
			for j in range(len(board)):
				try:
					index = boards[i][j].index(number)
					markedSpots[i].append((j,index))
				except ValueError:
					continue
		
		for i in range(len(markedSpots)):
			if len(markedSpots[i]) > 1:
				markedSpots[i].sort(key=lambda x:x[0]+0.1*x[1])
			for j in range(5):
				rows = filter(lambda x:x[0]==j, markedSpots[i])
				cols = filter(lambda x:x[1]==j, markedSpots[i])
				if len(list(rows)) == 5 or len(list(cols)) == 5:
					return i, markedSpots[i], number

winningBoardIndex, markedSpots, winningNumber = findWinningBoard(boards)
winningBoard = boards[winningBoardIndex]
result = 0
for i in range(len(winningBoard)):
	for j in range(len(winningBoard[i])):
		if (i, j) in markedSpots:
			continue
		result += int(winningBoard[i][j])

print(result * int(winningNumber))
		

				