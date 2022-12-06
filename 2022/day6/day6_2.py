data = ""
with open("input.txt", "r") as f:
   data = f.readline()

for i in range(len(data)-14):
   segment = data[i:i+14]
   s = set(segment)

   if len(s) == 14:
      print(i+14)
      break
