text = input("Enter message to decrypt: ")
dist = int(input("Enter ciphers distance: "))
decrypt = ""
for i in text:
  value = ord(i)
  cipherValue = value - dist
  if i == ' ':
    decrypt += ' '
    continue
  if cipherValue < ord('!'):
    cipherValue = (ord('~') - (dist + (ord('!') - value - 1)))
  decrypt += chr(int(cipherValue))
print(decrypt)
