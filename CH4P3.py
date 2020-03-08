choice = input("encrypt or decrypt?: ")
if choice == "encrypt":
  text = input("Enter file name to be encrypted: ")
  target = open(text, "r")
  encrypt = open("encrypted.txt", "w")
  dist = int(input("Enter distance for cipher: "))
  for x in target:
    for i in x:
      value = ord(i)
      cipherValue = value + dist
      if i == ' ':
        encrypt.write(' ')
        continue
      elif i == '\n':
        encrypt.write('\n')
        continue
      if cipherValue > ord('~'):
        cipherValue = ord('!') + dist - (ord('~') - value + 1)
      encrypt.write(chr(int(cipherValue)))
  target.close()
  encrypt.close()
elif choice == "decrypt":
  text = input("Enter the name of file to decrypt: ")
  target = open(text, "r")
  decrypt = open("decrypted.txt", "w")
  dist = int(input("Enter distance used for cipher: "))
  for x in target:
    for i in x:
      value = ord(i)
      cipherValue = value - dist
      if i == ' ':
        decrypt.write(' ')
        continue
      elif i == '\n':
        decrypt.write('\n')
        continue
      if cipherValue < ord('!'):
        cipherValue = ord('~') - (dist + (ord('!') - value - 1))
      decrypt.write(chr(int(cipherValue)))
  target.close()
  decrypt.close()
