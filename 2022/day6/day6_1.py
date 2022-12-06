data = ""
with open("input.txt", "r") as f:
   data = f.readline()

for i in range(len(data)-4):
   segment = data[i:i+4]
   s = set(segment)

   if len(s) == 4:
      print(i+4)
      break
