text = input("Enter the of the file to decrypt: ")
target = open(text, "r")
decrypt = open("decrypted.txt", "w")
dist = 1
char = ""
for x in target:
  for i in x:
    if i == ' ':
      bit = char
      rightShift = bit[len(bit)-1]
      firstInt = False
      length = len(bit)
      count = 1
      for integer in bit:
        if count == length:
          break
        rightShift += integer
        count += 1
      decimal = 0
      exponent = len(rightShift) - 1
      for digit in rightShift:
        decimal += int(digit) * 2 ** exponent
        exponent -= 1
      cipherValue = decimal - dist
      if cipherValue < ord('!'):
        cipherValue = ord('~')
      decrypt.write(chr(int(cipherValue)))
      char = ""
      continue
    elif i == 's':
      decrypt.write(' ')
      char = ""
      continue
    elif i == '\n':
      decrypt.write('\n')
      char = ""
      continue
    character += i
target.close()
decrypt.close()
print("Successfully decrypted file.")
