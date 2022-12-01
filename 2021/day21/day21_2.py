players = []
with open("example.txt", "r") as f:
	for line in f.readlines():
		line = line.strip()
		players.append([int(line[-1])-1, 0])

die = 0
dieRolls = 0
def dieRoll():
	global die, dieRolls
	die += 1
	dieRolls += 1
	if die > 100: die = 1
	return die

def turn(player):
	roll = 0
	for i in range(3):
		roll += dieRoll()
	
	player[0] = (player[0]+roll)%10
	player[1] += player[0]+1

running = True
while running:
	for i in range(len(players)):
		turn(players[i])
		if players[i][1] >= 21:
			print(players[i-1][1] * dieRolls)
			running = False