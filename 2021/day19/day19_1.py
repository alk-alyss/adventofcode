scanners = []
with open("example.txt", "r") as f:
	scanner = []
	for line in f.readlines():
		line = line.strip()
		if line.startswith("---"):
			continue
		if line == "":
			scanners.append(scanner)
			scanner = []
		else:
			line = list(map(int, line.split(',')))
			scanner.append(line)
	scanners.append(scanner)

def printScanner(scanner):
	for line in scanner:
		print(line)
	print()

# for scanner in scanners:
# 	printScanner(scanner)
print(len(scanners))
