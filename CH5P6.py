hexNum = {'10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}
def decimalToRep(num, base):
  num = int(num)
  total = ""
  remainder = 0
  while num != 0:
    temp = int(num / base)
    remainder = num % base
    num = temp
    if remainder >= 10:
      remainder = hexNum[str(remainder)]
    total += str(remainder)
  return total[::-1]
def main():
  print(decimalToRep("8", 8))
  print(decimalToRep("15", 5))
  print(decimalToRep("24", 14))
if __name__ == "__main__":
  main()
