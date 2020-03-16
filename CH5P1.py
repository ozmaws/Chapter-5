def main():
  num = [4,58,13,61,0,23,84,23]
  length = int(len(num))
  print("Median: " + str(median(num, length)))
  print("Mode: " + str(mode(num, length)))
  print("Mean: " + str(mean(num, length)))
def median(theList, length):
  if theList == []:
    return 0
  middle = theList[int(length / 2)]
  if middle % 2 == 0:
    medianNum = (middle + theList[int((length / 2) - 1)]) / 2
  else:
    medianNum = middle
  return medianNum
def mode(theList, length):
  if theList == []:
    return 0
  modeCount = 0
  for num in theList:
    count = 0
    for x in theList:
      if num == x:
        count += 1
      if x == theList[length - 1]:
        if count > modeCount:
          modeNum = num
          modeCount = count
  return modeNum
def mean(theList, length):
  if theList == []:
    return 0
  total = 0
  for num in theList:
    total += num
  meanNum = total / length
  return meanNum
if __name__ == "__main__":
  main()
