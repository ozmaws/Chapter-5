fileOne = input("Enter name of file you want number line for: ")
fileTwo = input("Enter name of file that you want the number line information to be stored in: ")
target = open(fileOne, "r")
numberCopy = open(fileTwo, "w")
count = 1
for line in target:
  numberCopy.write(str(count) + ">    " + line)
  count += 1
target.close()
numberCopy.close()
print("File numbered.")
