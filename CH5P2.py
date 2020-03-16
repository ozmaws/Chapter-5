filename = input("Input the name: ")
aFile = open(filename, "r")
count = 0
lines = []
for line in aFile:
  lines.append(line)
while True:
  print("\nThere are " + str(len(lines)) + " lines.")
  lineNum = int(input("Enter number, 0 to exit: "))
  if lineNum == 0:
    break
  print(lines[lineNum - 1])
aFile.close()
