with open("input.txt", "r") as f:
	# for i in range(6):
	# 	f.readline()
	line = f.readline().strip()

def hexToBin(hex):
	binary = ''
	for c in hex:
		b = bin(int(c, 16)).lstrip('0b').zfill(4)
		binary += b
	return binary

packets = hexToBin(line)
vSum = 0

def getPacketData(bits):
	global vSum
	v = int(bits[:3], 2)
	bits = bits[3:]
	t = int(bits[:3], 2)
	bits = bits[3:]
	vSum += v

	bitsRead = 6
	if t == 4:
		data = ''
		flag = True
		while flag:
			if bits[0] == '0': flag = False
			bits = bits[1:]
			data += bits[:4]
			bits = bits[4:]
			bitsRead += 5
		return data, bits
	else:
		bit = bits[0]
		bits = bits[1:]
		if bit == '0':
			length = int(bits[:15], 2)
			bits = bits[15:]
			subBits = bits[:length]
			bits = bits[length:]

			data = []
			while len(subBits)>0:
				subData, subBits = getPacketData(subBits)
				if isinstance(subData, str): subData = int(subData, 2)
				data.append(subData)

		elif bit == '1':
			subPackets = int(bits[:11], 2)
			bits = bits[11:]

			data = []
			for i in range(subPackets):
				subData, bits = getPacketData(bits)
				if isinstance(subData, str): subData = int(subData, 2)
				data.append(subData)
	
	if t==0:
		newData = sum(data)
	elif t==1:
		newData = 1
		for d in data:
			newData *= d
	elif t==2:
		newData = min(data)
	elif t==3:
		newData = max(data)
	elif t==5:
		newData = 1 if data[0]>data[1] else 0
	elif t==6:
		newData = 1 if data[0]<data[1] else 0
	elif t==7:
		newData = 1 if data[0]==data[1] else 0

	# print(t, data, newData)
	return newData, bits

while len(packets)>0:
	data, packets = getPacketData(packets)
	if '1' not in packets: break

print(data)
print(vSum)
