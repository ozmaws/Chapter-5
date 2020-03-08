#set up constants
text = input("Enter name of file to decrypt: ")
target = open(text, "r")
decryption = open("decrypted.txt", "w")
dist = int(input("Enter distance used: "))
#progam
for x in target:
  count = 0
  for i in x:
    toLower = i.lower()
    value = ord(toLower)
    cipherValue = value - dist
    if x[count] == ' ':
      decryption.write(' ')
      count += 1
      continue
    elif x[count] == '\n':
      decryption.write('\n')
      count += 1
      continue
    if cipherValue < ord('a'):
      cipherValue = ord('z') - (dist + (ord('a') - value - 1))
    decryption.write(chr(int(cipherValue)))
    count += 1

target.close()
decryption.close()
