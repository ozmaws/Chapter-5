choice = input("octal to decimal, or decimal to octal?: ")
if choice == "octal":
  octalNum = input("Enter octal number: ")
  decimal = 0
  exponent = len(octalNum) - 1
  for digit in octalNum:
    decimal += int(digit) * 8 ** exponent
    exponent -= 1
  print("The value is " + str(decimal))
if choice == "decimal":
  decimalNum = int(input("Enter decimal number: "))
  octal = ""
  if decimalNum == 0:
    print("The octal is 0")
  else:
    while decimalNum > 0:
      remainder = decimalNum % 8
      decimalNum = decimalNum // 8
      octal = str(remainder) + octal
    print("The octal is " + octal)
