def toBinary(a):
  m, n, = [], []
  string1 = ""
  for i in a:
   m.append(ord(i))
  for i in m:
   n.append(str(int(bin(i)[2:])))

  for i in n:
   string1 = string1 + i

  maxzeroes = 0
  maxones = 0
  print(n)
  zeroes = string1.split("1")
  ones = string1.split("0")

  for i in zeroes:
   if len(i) > maxzeroes:
    maxzeroes = len(i)
  for i in ones:
   if len(i) > maxones:
    maxones = len(i)

  print("Max sequence of zeroes is: ",maxzeroes)
  print("Max sequence of ones is: ", maxones)


file = open("two_cities_ascii.txt", "r")
filestring = file.read()

file.close()

toBinary(filestring)