choice = input("Left shift or right shift: ")
if choice == "left":
  bit = input("Input a bit to shift left: ")
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
  print(leftShift)
if choice == "right":
  bit = input("Input a bit to shift right: ")
  rightShift = bit[len(bit)-1]
  firstInt = False
  length = len(bit)
  count = 1
  for integer in bit:
    if count == length:
      break
    rightShift += integer
    count += 1
  print(rightShift)
