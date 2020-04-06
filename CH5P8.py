filename = input("Name of file: ")
input_file = open(filename, 'r')
output_file = open("concordance.txt", 'w')
words = []
freq = {}
count = 0
total = 0
for line in input_file:
  for word in line.split():
    words.append(word.lower())
words.sort()
for word in words:
  for w in words:
    if w == word:
      count += 1
  freq[word] = count
  count = 0
  total += 1
for (key, value) in frequency.items():
  output_file.write(key + ": " + str(('%.2f') % ((value / total) * 100)) + "%\n")
input_file.close()
output_file.close()
