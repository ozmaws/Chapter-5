text = input("Enter name of the file to encrypt: ")
target = open(text, "r")
encrypt = open("encrypted.txt", "w")
dist = 1
for x in target:
  for i in x:
    bit = ""
    value = ord(i)
    cipherValue = value + dist
    if i == ' ':
      encrypt.write('s')
      continue
    elif i == '\n':
      encrypt.write('\n')
      continue
    if cipherValue > ord('~'):
      cipherValue = ord('!')
    while cipherValue > 0:
      remainder = cipherValue % 2
      cipherValue = cipherValue // 2
      bit = str(remainder) + bit
    leftShift = ""
    firstInt = False
    length = len(bit)
    count = 1
    for integer in bit:
      if count == length:
        leftShift += bit[0]
        continue
      leftShift += bit[count]
      count += 1
    encrypt.write(leftShift + ' ')
target.close()
encrypt.close()
print("Encrypted file.")
