hexNumbers = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D': 13, 'E':14, 'F':15}
def repToDecimal(number, base):
  total = 0
  power = len(number) - 1
  for digit in number:
    total += hexNumbers[digit] * (base ** power)
    power -= 1
  return total
def main():
  print(repToDecimal("10", 8))
  print(repToDecimal("10", 16))
  print(repToDecimal("3F", 16))
  print(repToDecimal("4B", 12))
if __name__ == "__main__":
  main()
