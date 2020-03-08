text = input("Enter message to encrypt: ")
dist = int(input("Enter distance: "))
encrypt = ""
for i in text:
  value = ord(i)
  cipherValue = value + dist
  if i == ' ':
    encrypt += ' '
    continue
  if cipherValue > ord('~'):
    cipherValue = ord('!') + dist - (ord('~') - value + 1)
  encrypt += chr(int(cipherValue))
print(encrypt)
