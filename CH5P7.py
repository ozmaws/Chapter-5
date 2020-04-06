filename = input("File name: ")
input_file = open(filename, 'r')
output_file = open("sorted.txt", 'w')
words = []
for line in input_file:
  for word in line.split():
    words.append(word.lower())
words.sort()
for word in words:
  output_file.write(word)
  output_file.write('\n')
input_file.close()
output_file.close()
