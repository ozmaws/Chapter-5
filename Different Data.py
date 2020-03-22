from collections import deque
listStack = []
while len(listStack) < 6:
  num = input("Please enter number between 1-10: ")
  listStack.append(num)
print("Last number was " + listStack.pop())
print(listStack)
print()
listQueue = deque([])
while len(listQueue) < 5:
  print("While waiting, your number will be called, thank you.")
  print()
  listQueue.append(num) 
print(num + " ,thank you for waiting, please come to the window.")
print(listQueue)
