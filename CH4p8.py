fileOne = input("Enter name of file to be copied: ")
fileTwo = input("Enter name for file for the copied information: ")
target = open(fileOne, "r")
copy = open(fileTwo, "w")
for line in target:
  copy.write(line)
target.close()
copy.close()
print("File copied.")
