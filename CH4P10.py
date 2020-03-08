fileOne = input("Enter the name of the first file: ")
fileTwo = input("Enter the name of the second file: ")
target1 = open(fileOne, "r")
target2 = open(fileTwo, "r")
same = True
count = 0
while True:
  count += 1
  storedLine1 = target1.readline()
  storedLine2 = target2.readline()
  if storedLine1 != storedLine2:
    same = False
    break
  elif storedLine1 == '' or storedLine2 == '':
    break
if same:
  print("Yes.")
else:
  print("No.")
  print(fileOne + " reads '" + storedLine1 + "' at line " + str(count))
  print(fileTwo + " reads '" + storedLine2 + "' at line " + str(count))
target1.close()
target2.close()
