#set up for constants
text = input("Enter message to be encrypted: ")
encryption = open("encrypted.txt", "w")
dist = int(input("Enter the distance of the cipher: "))
#program
for i in text:
  toLower = i.lower()
  value = ord(toLower)
  cipherValue = value + dist
  if i == ' ':
    encryption.write(' ')
    continue
  if cipherValue > ord('z'):
    cipherValue = ord('a') + dist - (ord('z') - value + 1)
  encryption.write(chr(int(cipherValue)))
encryption.close()
